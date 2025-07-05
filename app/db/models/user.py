#!/usr/bin/python3
"""user model"""

from sqlmodel import Field
from .base_model import BaseModel
from typing import Optional


class User(BaseModel, table=True):
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    picture: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False
    google_sub: Optional[str] = Field(index=True, unique=True)
    provider: str
    role: Optional[str] = "user"
    hashed_password: Optional[str] = None
    

    class Config:
        arbitrary_types_allowed = True
