from fastapi import APIRouter, Request
from services.response import get_bot_reply

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    reply = get_bot_reply(message)
    return {"response": reply}
