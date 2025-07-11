from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ChatRequest(BaseModel):
    user_id: str
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "คุณคือ LegalGPT นักกฎหมายผู้เชี่ยวชาญด้านกฎหมายไทยทุกแขนง ให้ช่วยตอบคำถามทางกฎหมายอย่างเป็นทางการและถูกต้อง"},
            {"role": "user", "content": req.question}
        ],
        temperature=0.2
    )
    return {"answer": resp.choices[0].message.content}
