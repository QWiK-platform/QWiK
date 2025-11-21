from pydantic import BaseModel
from typing import List, Literal
from datetime import datetime

# 로그 한 줄
class LogEntry(BaseModel):
    timestamp: datetime
    level: Literal["info", "warning", "error", "success"]
    message: str

# 빌드 로그 응답
class BuildLogsResponse(BaseModel):
    deployment_id: int
    status: Literal["queued", "building", "success", "failed"]
    logs: List[LogEntry]