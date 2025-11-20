from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv


load_dotenv()


app = FastAPI(
    title="QWiK API",
    description="배포를 쉽고 빠르게! QWiK 백엔드 API",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "QWiK API is running! 🚀",
        "status": "healthy"
    }


@app.on_event("startup")
async def startup_event():
    print("🚀 Started!")
    print(f"📝 Docs: http://localhost:8000/docs")