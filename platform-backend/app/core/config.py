from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):

    DATABASE_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str
    GITHUB_REDIRECT_URI: str
    
    FRONTEND_URL: str
    
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 싱글톤 인스턴스
settings = Settings()