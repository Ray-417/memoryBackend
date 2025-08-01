from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.deepseek import chat_with_deepseek

router = APIRouter()

@router.post("/chat")
async def chat(req: ChatRequest):
    reply = await chat_with_deepseek(req.messages)
    return {"reply": reply}
