#!/usr/bin/python3
"""Main module for the application"""

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import init_db
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.core.middleware.logging import RequestLoggingMiddleware
from loguru import logger
from app.utils.json_response import JSONResponseDict


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan of the application"""
    logger.info("Starting up...")
    await init_db()
    yield
    logger.info("Shutting down...")


setup_logging()

app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

origins = [
    "http://localhost:8000",
    "http://localhost:8001",
]

app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Home"])
async def get_root(request: Request):
    """Root endpoint"""
    return JSONResponseDict(
        message="Welcome to the API", status_code=status.HTTP_200_OK, data={"URL": ""}
    )


@app.get("/health")
def health_check():
    """Checks the health of the application"""
    logger.debug("Health check endpoint called")
    return {
        "status": "OK",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_description": settings.APP_DESCRIPTION,
        "app_contact_email": settings.APP_CONTACT_EMAIL,
        "app_contact_url": settings.APP_CONTACT_URL,
        "app_contact_phone": settings.APP_CONTACT_PHONE,
    }


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, reload=True)
