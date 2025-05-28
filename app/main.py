#!/usr/bin/python3

"""
Entry point to taskhive application
"""
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request

from app.core.config import settings
from app.core.i18n import t
from app.core.middleware import LocaleMiddleware
from app.database.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    print("Server is shutting down")


app = FastAPI(lifespan=lifespan)

# Add locale middleware
app.add_middleware(LocaleMiddleware)


@app.get("/health")
def health_check():
    """Checks the health of the application"""
    return {"status": "OK"}


@app.get("/welcome")
async def welcome(request: Request):
    """Welcome endpoint with i18n support"""
    locale = request.state.locale
    return {"message": t("common.welcome", locale=locale), "locale": locale}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
