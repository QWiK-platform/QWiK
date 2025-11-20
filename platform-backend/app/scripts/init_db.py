"""
데이터베이스 초기화 스크립트
최초 1회 또는 필요 시에만 실행
"""
import sys
from pathlib import Path

# 프로젝트 루트를 Python path에 추가
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.core.database import Base, engine, SessionLocal
from app.core.config import settings
from app.models.user import User

def init_db():
    """
    데이터베이스 테이블 생성
    """
    print("=" * 50)
    print("🗄️  Database Initialization")
    print("=" * 50)
    print(f"Database URL: {settings.DATABASE_URL}")
    print()
    
    try:
        # 테이블 생성
        print("📦 Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully!")
        
        # 테이블 목록 확인
        print("\n📋 Created tables:")
        for table in Base.metadata.sorted_tables:
            print(f"  - {table.name}")
        
        print("\n🎉 Database initialization complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

def drop_db():
    """
    데이터베이스 테이블 삭제 (주의!)
    """
    print("=" * 50)
    print("⚠️  WARNING: Dropping all tables")
    print("=" * 50)
    
    confirm = input("Are you sure? Type 'yes' to confirm: ")
    
    if confirm.lower() == 'yes':
        try:
            Base.metadata.drop_all(bind=engine)
            print("✅ All tables dropped!")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        print("❌ Cancelled")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Database management")
    parser.add_argument(
        "command",
        choices=["init", "drop"],
        help="Command to run"
    )
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_db()
    elif args.command == "drop":
        drop_db()