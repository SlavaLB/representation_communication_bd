from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from domain.one_to_one import OneToOne

# Асинхронный engine
engine_async = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine_async, class_=AsyncSession, expire_on_commit=False)


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


def get_one_to_one(session: AsyncSession = Depends(get_async_db)) -> OneToOne:
    """Фабрика для создания экземпляра OneToOne"""
    return OneToOne(session)
