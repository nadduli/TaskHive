#!/usr/bin/python3
"""database module"""

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from typing import AsyncGenerator

from app.core.config import settings

engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=False,
)


async def init_db():
    """Initialize the database"""
    async with engine.begin() as conn:
        from app.models.user import User

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a session for the database"""
    async_session = AsyncSession(engine, expire_on_commit=False)
    async with async_session as session:
        yield session
