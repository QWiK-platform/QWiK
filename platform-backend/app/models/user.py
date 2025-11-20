from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


# user 테이블
class User(Base):

    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    github_id = Column(String(50), unique=True, nullable=False, index=True)
    github_username = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(user_id={self.user_id}, github_username={self.github_username})>"