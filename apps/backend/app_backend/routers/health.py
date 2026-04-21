from datetime import datetime, timezone

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(tags=["meta"])


class HealthResponse(BaseModel):
    status: str
    db: str
    redis: str
    timestamp: str


@router.get("/health", response_model=HealthResponse)
async def health(request: Request) -> HealthResponse:
    db_status = "ok"
    redis_status = "ok"

    try:
        await request.app.state.db.command("ping")
    except Exception:
        db_status = "error"

    try:
        await request.app.state.redis.ping()
    except Exception:
        redis_status = "error"

    overall = "ok" if db_status == "ok" and redis_status == "ok" else "degraded"
    return HealthResponse(
        status=overall,
        db=db_status,
        redis=redis_status,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
