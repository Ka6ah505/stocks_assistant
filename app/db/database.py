"""
created: 2022-02-15
by: Mironov Sergei [ka6ah505@gmail.com]
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.pool import NullPool

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

LINK_CONNECT_TO_BASE = f'postgresql+asyncpg://' \
                       f'{DB_USER}:{DB_PASS}@' \
                       f'{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(LINK_CONNECT_TO_BASE, poolclass=NullPool)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
