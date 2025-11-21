from fastapi import APIRouter, Depends, HTTPException, Header
from app.schemas.deployment import BuildLogsResponse
from app.services.deployment_service import get_dummy_build_logs
from app.core.security import verify_token

router = APIRouter(
    prefix="/deployments",
    tags=["Deployments"]
)

def get_current_user_id(authorization: str = Header(None)) -> int:
    """
    Authorization 헤더에서 JWT 토큰 검증
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    
    return user_id

@router.get("/{deployment_id}/logs", response_model=BuildLogsResponse)
async def get_build_logs(
    deployment_id: int,
    user_id: int = Depends(get_current_user_id)
):
    """
    빌드 로그 조회
    
    deployment_id에 따라 다른 상태 반환 (더미 데이터):
    - deployment_id % 2 == 0: queued
    - deployment_id % 3 == 0: building
    - deployment_id % 4 == 0: failed
    - 그 외: success
    
    나중에 실제 배포 시스템과 연동 예정
    """
    return get_dummy_build_logs(deployment_id)