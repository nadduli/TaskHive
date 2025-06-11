#!/usr/bin/python3
"""settings module"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class Settings(BaseSettings):
    """Settings for the application"""

    POSTGRES_URL: str
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
