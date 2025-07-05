#!/usr/bin/python3
"""Base Model module"""

from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime

def utcnow():
    """Return a naive UTC datetime (compatible with PostgreSQL TIMESTAMP WITHOUT TIME ZONE)."""
    return datetime.utcnow()

class BaseModel(SQLModel):
    """Base model with UUID primary key and timestamp fields."""

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    created_at: datetime = Field(default_factory=utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=utcnow,
        nullable=False,
        sa_column_kwargs={"onupdate": utcnow}
    )
