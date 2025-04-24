import os
import logging
from typing import Optional, List, TypedDict

from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mcp_client")

# Define the shape of LangGraph state
class State(TypedDict, total=False):
    thread: List
    tool_calls: List

# Conversation memory store (in-memory for now)
_conversations = {}

# Load environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_PYTHON_URL = os.getenv("MCP_PYTHON_URL")

logger.info(f"Using MCP Server URL: {MCP_PYTHON_URL}")

model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)

async def load_tools():
    logger.info("Loading MCP tools from server...")
    try:
        async with MultiServerMCPClient({
            "mcp": {"base_url": MCP_PYTHON_URL}
        }) as client:
            tools = await load_mcp_tools(client)
            logger.info(f"Successfully loaded {len(tools)} tools from MCP server: {[tool.name for tool in tools]}")
            return tools
    except Exception as e:
        logger.error(f"Error loading tools from MCP server: {str(e)}")
        raise

async def call_llm(state: State) -> State:
    messages = state.get("thread", [])
    logger.info(f"Calling LLM with {len(messages)} messages")
    response = await model.ainvoke(messages)
    messages.append(response)
    tool_calls = getattr(response, "tool_calls", [])
    if tool_calls:
        logger.info(f"LLM requesting tool calls: {[call['name'] for call in tool_calls]}")
    else:
        logger.info("LLM response contains no tool calls")
    return {"thread": messages, "tool_calls": tool_calls}

async def call_tools(state: State) -> State:
    tool_calls = state.get("tool_calls", [])
    if not tool_calls:
        logger.info("No tool calls to execute")
        return state

    logger.info(f"Executing {len(tool_calls)} tool calls")
    try:
        tools = await load_tools()
        tool_names = [tool.name for tool in tools]
        logger.info(f"Available tools: {tool_names}")
        
        outputs = []
        for call in tool_calls:
            logger.info(f"Processing tool call: {call['name']} with args: {call['args']}")
            tool = next((t for t in tools if t.name == call["name"]), None)
            if tool:
                logger.info(f"Found matching tool: {tool.name}")
                args = call["args"]
                try:
                    logger.info(f"Invoking tool {tool.name} with args {args}")
                    result = await tool.ainvoke(args)
                    logger.info(f"Tool {tool.name} returned: {result}")
                    outputs.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
                except Exception as e:
                    error_msg = f"Error executing tool {tool.name}: {str(e)}"
                    logger.error(error_msg)
                    outputs.append(ToolMessage(content=error_msg, tool_call_id=call["id"]))
            else:
                error_msg = f"Tool '{call['name']}' not found in available tools: {tool_names}"
                logger.warning(error_msg)
                outputs.append(ToolMessage(content=error_msg, tool_call_id=call["id"]))

        return {"thread": state["thread"] + outputs, "tool_calls": []}
    except Exception as e:
        logger.error(f"Error in call_tools: {str(e)}")
        return {"thread": state["thread"], "tool_calls": []}

def has_tool_calls(state: State) -> str:
    tool_calls = state.get("tool_calls", [])
    result = "tools" if tool_calls else END
    logger.info(f"has_tool_calls check: returning '{result}'")
    return result

# Define the LangGraph
tools_graph = StateGraph(State)
tools_graph.add_node("llm", call_llm)
tools_graph.add_node("tools", call_tools)
tools_graph.set_entry_point("llm")
tools_graph.add_conditional_edges("llm", has_tool_calls)
tools_graph.add_edge("tools", "llm")
tools_graph.set_finish_point("llm")

agent = tools_graph.compile()

async def process_message(message: str, conversation_id: str = "default") -> str:
    logger.info(f"Processing message in conversation '{conversation_id}': {message}")
    # Retrieve or start conversation history
    thread = _conversations.get(conversation_id, [])
    thread.append(HumanMessage(content=message))

    state = {"thread": thread}
    logger.info(f"Invoking agent with initial state (thread length: {len(thread)})")
    result = await agent.ainvoke(state)
    logger.info(f"Agent completed with final thread length: {len(result['thread'])}")

    # Save updated thread
    _conversations[conversation_id] = result["thread"]

    # Get the most recent AI message
    ai_messages = [msg for msg in result["thread"] if isinstance(msg, AIMessage)]
    if ai_messages:
        response = ai_messages[-1].content
        logger.info(f"Returning AI response: {response[:100]}...")  # Log first 100 chars
        return response
    logger.warning("No AI message found in result thread")
    return "No valid response."
