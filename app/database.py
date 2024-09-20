"""Database configuration"""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings

Base = declarative_base()

async_engine = create_async_engine(
    settings.DATABASE_URL, 
    future=True,
    echo=True,
)

local_session = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get database session"""
    async_session = local_session
    async with async_session() as db:
        yield db
