#!/usr/bin/python3
"""This module defines a user model"""

from sqlmodel import Field
from typing import Optional
from .base_model import BaseModel


class User(BaseModel, table=True):
    """
    A User class that represents a user in the database

    Attributes:
        uid: The unique identifier for the user
        email: The email of the user
        first_name: The user's first name
        last_name: The user's last name
        password: The password of the user
        avatar: URL to the user's avatar image
        is_active: Whether the user account is active
        created_at: The timestamp of the user's creation
        updated_at: The timestamp of the user's last update
    """

    __tablename__ = "users"

    first_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
    avatar: Optional[str] = Field(nullable=True)
    is_active: bool = Field(default=True)

    @property
    def full_name(self) -> str:
        """Get the user's full name"""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User(uid={self.uid}, email={self.email}, name={self.full_name})"
