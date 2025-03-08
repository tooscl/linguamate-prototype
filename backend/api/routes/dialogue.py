from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.chat_ai import get_ai_response

router = APIRouter()

class Message(BaseModel):
    user_id: str
    text: str

@router.post("/message")
async def send_message(data: Message):
    response = get_ai_response(data.text)
    return {"response": response}
