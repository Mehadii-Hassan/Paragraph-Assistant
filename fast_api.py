from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio

from paragraph_assistant import generate_paragraph

app = FastAPI()

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can limit this for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    topic = data.get("prompt", "")
    if not topic.strip():
        return JSONResponse({"error": "Prompt cannot be empty"}, status_code=400)

    output = await generate_paragraph(topic)
    return JSONResponse({"result": output})
