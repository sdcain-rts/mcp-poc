from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import LangGraphAgent

# Initialize the FastAPI application
app = FastAPI()

# Define the request model for the /chat endpoint
class ChatRequest(BaseModel):
    message: str  # The user message to be processed

# Initialize the LangGraph agent
agent = LangGraphAgent()

# Define the /chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint to process user messages.
    - Accepts a JSON payload with a "message" field.
    - Uses the LangGraph agent to process the message and return a response.
    """
    try:
        response = agent.process_message(request.message)  # Process the message using the agent
        return {"response": response}  # Return the response as JSON
    except Exception as e:
        # Handle any errors and return a 500 status code
        raise HTTPException(status_code=500, detail=str(e))