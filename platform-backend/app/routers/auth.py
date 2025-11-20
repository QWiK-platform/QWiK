from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import GitHubCallbackRequest, TokenResponse
from app.services.auth_service import github_login

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/github/callback", response_model=TokenResponse)
async def github_callback(
    request: GitHubCallbackRequest,
    db: Session = Depends(get_db)
):
    """
    GitHub OAuth 콜백
    
    프론트엔드에서 GitHub에서 받은 code를 전달하면
    JWT Access Token을 반환합니다.
    """
    try:
        token = await github_login(request.code, db)
        return token
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")