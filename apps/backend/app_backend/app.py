import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app_backend.config import settings
from app_backend.db import close_mongodb, close_redis, connect_mongodb, connect_redis
from app_backend.middleware import RequestIDMiddleware
from app_backend.routers import health

logger = logging.getLogger(__name__)


sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # motor = await connect_mongodb()
    # app.state.motor = motor
    # app.state.db = motor[settings.mongodb_db]
    # app.state.redis = await connect_redis()
    # logger.info("MongoDB and Redis connected")
    # yield
    # await close_mongodb()
    # await close_redis()
    # logger.info("MongoDB and Redis disconnected")
    pass


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # Middleware — outermost wrapper first
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(SentryAsgiMiddleware)

    # JSON error handlers
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
        request_id = getattr(request.state, "request_id", "")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail, "request_id": request_id},
            headers=getattr(exc, "headers", None) or {},
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        request_id = getattr(request.state, "request_id", "")
        logger.exception("Unhandled error [request_id=%s]", request_id)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "request_id": request_id},
        )

    # Routers
    app.include_router(health.router)
    # app.include_router(example_router, prefix=settings.API_PREFIX)

    if settings.ENV == "dev":
        from app_backend.routers import _test_runner
        app.include_router(_test_runner.router)
    
    return app
