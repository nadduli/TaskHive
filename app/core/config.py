#!/usr/bin/python3
"""settings module"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class JWTSettings(BaseModel):
    secret_key: str = ""
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_minutes: int = 10080  # 7 days


class Settings(BaseSettings):
    """Settings for the application"""

    POSTGRES_URL: str
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_CONTACT_EMAIL: str
    APP_CONTACT_URL: str
    APP_CONTACT_PHONE: str

    # JWT Settings
    jwt_settings: JWTSettings = JWTSettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_nested_delimiter="__",
    )


settings = Settings()
