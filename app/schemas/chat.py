from pydantic import BaseModel

class ChatRequest(BaseModel):
    messages: list[dict]  # [{"role": "user", "content": "..."}]
