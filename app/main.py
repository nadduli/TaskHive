#!/usr/bin/python3
"""Entry point to my application"""

from fastapi import FastAPI
from app.core.config import get_settings
from app.db.session import init_db
from app.api.v1.routes import auth, health
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from app.core.logger import logger


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services"""
    await init_db()
    yield
    logger.info("Shutting down")


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])


@app.get("/", include_in_schema=False)
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG
    )
