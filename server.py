from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import Assistant
from prompts import SESSION_INSTRUCTION

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/ask")
async def ask(request: Request):
    data = await request.json()
    user_text = data.get("text", "")
    assistant = Assistant()
    reply = await assistant.generate_reply(SESSION_INSTRUCTION, user_text)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=5000, reload=True)