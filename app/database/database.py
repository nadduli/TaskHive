#!/usr/bin/python3

"""Database connection and initialization module.
This module provides a function to create a database connection and
initialize the database with the required tables.
"""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import text
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings

async_engine = create_async_engine(url=settings.POSTGRES_URL, echo=True)


async def init_db():
    async with AsyncSession(async_engine) as session:
        statement = text("SELECT 'hello';")
        result = await session.exec(statement)
        print(result)
