from motor.motor_asyncio import AsyncIOMotorClient
from redis.asyncio import Redis
from redis.asyncio import from_url as redis_from_url

from app_backend.config import settings

_motor_client: AsyncIOMotorClient | None = None
_redis_client: Redis | None = None


async def connect_mongodb() -> AsyncIOMotorClient:
    global _motor_client
    _motor_client = AsyncIOMotorClient(
        settings.mongodb_url,
        minPoolSize=5,
        maxPoolSize=20,
    )
    return _motor_client


async def close_mongodb() -> None:
    global _motor_client
    if _motor_client is not None:
        _motor_client.close()
        _motor_client = None


async def connect_redis() -> Redis:
    global _redis_client
    _redis_client = redis_from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )
    return _redis_client


async def close_redis() -> None:
    global _redis_client
    if _redis_client is not None:
        await _redis_client.aclose()
        _redis_client = None
