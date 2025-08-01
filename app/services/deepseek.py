import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
print("API_KEY loaded:", API_KEY is not None)  # 应该为 True

async def chat_with_deepseek(messages: list[dict]) -> str:
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.7
    }

    print("=== Sending Request ===")
    print("Payload:", payload)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        print("Response status:", response.status_code)
        print("Response body:", response.text)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
