from datetime import datetime, timedelta
from app.schemas.deployment import BuildLogsResponse, LogEntry
from fastapi import HTTPException

def get_dummy_build_logs(deployment_id: int) -> BuildLogsResponse:
    """
    더미 빌드 로그 반환
    나중에 실제 로그 스트리밍으로 대체 예정
    """
    
    # deployment_id 검증 1~10 까지만
    if deployment_id < 1 or deployment_id > 10:
        raise HTTPException(status_code=404, detail="Deployment not found")
    
    # 현재 시간 기준
    now = datetime.utcnow()
    
    # 더미 로그 생성
    dummy_logs = [
        LogEntry(
            timestamp=now - timedelta(seconds=60),
            level="info",
            message="🚀 Starting deployment process..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=58),
            level="info",
            message="📦 Cloning repository from GitHub..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=55),
            level="success",
            message="✅ Repository cloned successfully"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=52),
            level="info",
            message="📥 Installing dependencies..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=50),
            level="info",
            message="npm install --production"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=35),
            level="info",
            message="added 245 packages in 15s"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=34),
            level="success",
            message="✅ Dependencies installed"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=32),
            level="info",
            message="🔨 Building application..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=30),
            level="info",
            message="npm run build"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=28),
            level="info",
            message="Creating optimized production build..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=20),
            level="info",
            message="Compiled successfully!"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=18),
            level="info",
            message="File sizes after gzip:"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=17),
            level="info",
            message="  dist/main.js    142.5 kB"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=16),
            level="info",
            message="  dist/vendors.js 89.3 kB"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=15),
            level="success",
            message="✅ Build completed successfully"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=13),
            level="info",
            message="🌐 Deploying to production..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=10),
            level="info",
            message="Uploading build artifacts..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=5),
            level="info",
            message="Configuring CDN..."
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=2),
            level="success",
            message="✅ Deployment successful!"
        ),
        LogEntry(
            timestamp=now - timedelta(seconds=1),
            level="success",
            message=f"🎉 Your app is live at: https://qwik-demo-{deployment_id}.vercel.app"
        ),
    ]
    
    # deployment_id에 따라 다른 상태 반환 (테스트용)
    if deployment_id % 4 == 0:
        status = "failed"
        # 실패 로그 추가
        dummy_logs.append(
            LogEntry(
                timestamp=now,
                level="error",
                message="❌ Build failed: Module not found"
            )
        )
    elif deployment_id % 3 == 0:
        status = "building"
        # 진행 중 로그만
        dummy_logs = dummy_logs[:10]
    elif deployment_id % 2 == 0:
        status = "queued"
        dummy_logs = [
            LogEntry(
                timestamp=now,
                level="info",
                message="⏳ Deployment queued. Waiting for available resources..."
            )
        ]
    else:
        status = "success"
    
    return BuildLogsResponse(
        deployment_id=deployment_id,
        status=status,
        logs=dummy_logs
    )