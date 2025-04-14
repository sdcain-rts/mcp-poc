import os
from typing import Optional, List, TypedDict

from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

# Define the shape of LangGraph state
class State(TypedDict, total=False):
    thread: List

# Conversation memory store (in-memory for now)
_conversations = {}

# Load environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_PYTHON_URL = os.getenv("MCP_PYTHON_URL")

model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)

async def load_tools():
    async with MultiServerMCPClient({
        "mcp": {"base_url": MCP_PYTHON_URL}
    }) as client:
        return await load_mcp_tools(client)

async def call_llm(state: State) -> State:
    messages = state.get("thread", [])
    response = await model.ainvoke(messages)
    messages.append(response)
    tool_calls = getattr(response, "tool_calls", [])
    return {"thread": messages, "tool_calls": tool_calls}

async def call_tools(state: State) -> State:
    tool_calls = state.get("tool_calls", [])
    if not tool_calls:
        return state

    tools = await load_tools()
    outputs = []
    for call in tool_calls:
        tool = next(t for t in tools if t.name == call["name"])
        args = call["args"]
        result = await tool.ainvoke(args)
        outputs.append(ToolMessage(content=str(result), tool_call_id=call["id"]))

    return {"thread": state["thread"] + outputs}

# Define the LangGraph
tools_graph = StateGraph(State)
tools_graph.add_node("llm", call_llm)
tools_graph.add_node("tools", call_tools)
tools_graph.set_entry_point("llm")
tools_graph.add_conditional_edges("llm", lambda state: "tools" if state.get("tool_calls") else "llm")
tools_graph.add_edge("tools", "llm")
tools_graph.set_finish_point("llm")

agent = tools_graph.compile()

async def process_message(message: str, conversation_id: str = "default") -> str:
    # Retrieve or start conversation history
    thread = _conversations.get(conversation_id, [])
    thread.append(HumanMessage(content=message))

    state = {"thread": thread}
    result = await agent.ainvoke(state)

    # Save updated thread
    _conversations[conversation_id] = result["thread"]

    for msg in result["thread"]:
        if isinstance(msg, AIMessage):
            return msg.content
    return "No valid response."
