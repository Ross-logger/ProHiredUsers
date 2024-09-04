# import pytest
# from typing import AsyncGenerator
# from httpx import AsyncClient
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from fastapi.testclient import TestClient
#
# from src.database.database import Base, get_async_session
# from src.main import app
# from config import TEST_DB_HOST, TEST_DB_NAME, TEST_DB_PASS, TEST_DB_PORT, TEST_DB_USER
# import asyncio
#
# DATABASE_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"
#
# # Create the async engine and session maker for the test database
# test_async_engine = create_async_engine(DATABASE_URL, echo=True)
# async_session_maker = async_sessionmaker(test_async_engine, class_=AsyncSession, expire_on_commit=False)
#
# # Bind the metadata to the test engine
# Base.metadata.bind = test_async_engine
#
#
# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
#
#
# app.dependency_overrides[get_async_session] = override_get_async_session
#
#
# @pytest.fixture(scope='session', autouse=True)
# async def database_setup():
#     async with test_async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     async with test_async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#
#
