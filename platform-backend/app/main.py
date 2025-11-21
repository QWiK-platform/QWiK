from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.routers import auth, users, deployment


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


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(deployment.router)


@app.get("/")
async def root():
    return {
        "message": "QWiK API is running! 🚀",
        "status": "healthy"
    }
