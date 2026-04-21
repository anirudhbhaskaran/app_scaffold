import logging
from fastapi import APIRouter, HTTPException

from app_backend.tests import health  # import all test modules here

logger = logging.getLogger(__name__)
router = APIRouter()

TEST_MAP = {
    "health": health.test_health,
}


@router.get("/test")
async def run_test(route: str):
    logger.info("test_runner called for route=%s", route)

    if route not in TEST_MAP:
        logger.error("test not found for route=%s", route)
        raise HTTPException(status_code=404, detail="Test not found")

    try:
        result = TEST_MAP[route]()
        logger.info("test passed for route=%s", route)
        return result
    except Exception as e:
        logger.exception("test failed for route=%s", route)
        raise HTTPException(status_code=500, detail=str(e))
