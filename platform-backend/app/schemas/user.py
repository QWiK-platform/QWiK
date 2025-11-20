from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 사용자 생성 (내부용)
class UserCreate(BaseModel):
    github_id: str
    github_username: str
    email: Optional[str] = None

# 사용자 응답
class UserResponse(BaseModel):
    user_id: int
    github_id: str
    github_username: str
    email: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True