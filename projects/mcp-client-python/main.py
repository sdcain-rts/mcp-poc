from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import process_message

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    conversation_id: str = "default"  # Optional conversation tracking

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = await process_message(
            message=request.message,
            conversation_id=request.conversation_id
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
