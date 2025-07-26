import os
from master_agent.agent import root_agent
from vertexai.preview.reasoning_engines import AdkApp
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

adk_app = AdkApp(agent=root_agent)
app = FastAPI()
PORT = os.getenv("PORT", 8000)

class QueryInput(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat(input: QueryInput):
    response_stream = adk_app.stream_query(user_id=input.user_id, message=input.message)
    response_text = ""
    for chunk in response_stream:
        response_text += chunk["content"]["parts"][0].get("text", "")
    return {"response": response_text}

def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)

if __name__ == "__main__":
    main()