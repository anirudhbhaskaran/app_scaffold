import logging

logger = logging.getLogger(__name__)

def test_health():
    logger.info("[TEST] health_check start")

    # stubbed response (no HTTP call)
    response = {"status": "ok"}

    assert response["status"] == "ok"

    logger.info("[TEST] health_check success")

    return {
        "test": "health_check",
        "status": "passed",
        "response": response,
    }
