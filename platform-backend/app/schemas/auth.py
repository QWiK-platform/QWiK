from pydantic import BaseModel
from typing import Optional

# GitHub OAuth 콜백 요청
class GitHubCallbackRequest(BaseModel):
    code: str

# JWT 토큰 응답
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"