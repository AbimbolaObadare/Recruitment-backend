import asyncio
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi_users.db import SQLAlchemyUserDatabase
from typing import AsyncGenerator
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from db.base import Base


from db.models.users import User
from db.models.auth import AccessToken
import databases


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./dev.db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL,echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def create_tables():
    print("Database Created")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


task = asyncio.create_task(create_tables())


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
