#!/usr/bin/python3

"""This module defines a base model for all models"""

from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID, TIMESTAMP
from sqlalchemy import Column


class BaseModel(SQLModel):
    """A base class for all skill bridge models
    Attributes:
        uid: The unique identifier for the model
        created_at: The timestamp of the model's creation
        update_at: The timestamp of the model's last update
    """

    uid: UUID = Field(
        default_factory=uuid4, sa_type=PostgresUUID(as_uuid=True), primary_key=True
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=TIMESTAMP(timezone=True),
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            onupdate=datetime.now(timezone.utc),
        ),
    )
