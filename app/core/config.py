#!/usr/bin/python3
"""Configuration module"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "Skill Bridge"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Skill Bridge API"
    DEBUG: bool = False
    SECRET_KEY: str

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    CORS_ORIGINS: List[str] = ["http://localhost:8000"]

    DATABASE_URL: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
