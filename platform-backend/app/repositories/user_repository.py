from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from typing import Optional


# GitHub ID로 사용자 조회
def get_user_by_github_id(db: Session, github_id: str) -> Optional[User]:
    
    return db.query(User).filter(User.github_id == github_id).first()


# User ID로 사용자 조회
def get_user_by_id(db: Session, user_id: int) -> Optional[User]:

    return db.query(User).filter(User.user_id == user_id).first()


# 사용자 생성
def create_user(db: Session, user_data: UserCreate) -> User:

    db_user = User(
        github_id=user_data.github_id,
        github_username=user_data.github_username,
        email=user_data.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 사용자 조회 또는 생성 (로그인 시 사용)
def get_or_create_user(db: Session, user_data: UserCreate) -> User:

    # 기존 사용자 확인
    user = get_user_by_github_id(db, user_data.github_id)
    
    if user:
        # 정보 업데이트 (username이나 email이 바뀔 수 있음)
        user.github_username = user_data.github_username
        user.email = user_data.email
        db.commit()
        db.refresh(user)
        return user
    
    # 새 사용자 생성
    return create_user(db, user_data)