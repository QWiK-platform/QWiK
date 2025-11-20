import httpx
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.config import settings
from app.core.security import create_access_token
from app.repositories.user_repository import get_or_create_user
from app.schemas.user import UserCreate
from app.schemas.auth import TokenResponse
from fastapi import HTTPException

async def exchange_code_for_token(code: str) -> str:
    """
    GitHub Authorization Code를 Access Token으로 교환
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            data={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={"Accept": "application/json"}
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to exchange code for token")
        
        data = response.json()
        
        if "error" in data:
            raise HTTPException(status_code=400, detail=data.get("error_description", "GitHub OAuth error"))
        
        return data["access_token"]

async def get_github_user_info(access_token: str) -> dict:
    """
    GitHub Access Token으로 사용자 정보 가져오기
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json"
            }
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to get user info from GitHub")
        
        return response.json()

async def github_login(code: str, db: Session) -> TokenResponse:
    """
    GitHub OAuth 로그인 전체 플로우
    """
    # 1. Code → GitHub Access Token
    github_token = await exchange_code_for_token(code)
    
    # 2. GitHub Access Token → 사용자 정보
    github_user = await get_github_user_info(github_token)
    
    # 3. DB에 사용자 저장/조회
    user_data = UserCreate(
        github_id=str(github_user["id"]),
        github_username=github_user["login"],
        email=github_user.get("email")
    )
    
    user = get_or_create_user(db, user_data)
    
    # 4. JWT 생성
    access_token = create_access_token(
        data={"user_id": user.user_id, "github_username": user.github_username},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return TokenResponse(access_token=access_token, token_type="bearer")