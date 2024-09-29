import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient, MockTransport, Response
from src.main import app
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.database.database import get_async_session, Base
from config import TEST_DB_HOST, TEST_DB_NAME, TEST_DB_PASS, TEST_DB_PORT, TEST_DB_USER
from typing import AsyncGenerator
from tests.utils import register_user, login, about_me

# DATABASE_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"
#
# test_async_engine = create_async_engine(DATABASE_URL, echo=True)
# async_session_maker = async_sessionmaker(test_async_engine, expire_on_commit=False)
#
#
# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
#
#
# app.dependency_overrides[get_async_session] = override_get_async_session
#
# DATABASE_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"
#

@pytest.fixture(scope="module")
async def her():
    print("HER!")
    yield  # Ensure the fixture is an async generator

@pytest.mark.asyncio(loop_scope="module")
async def test_auth(her):
    print("Sam HER!")

# @pytest.fixture(scope="session", autouse=True)
# async def setup_database():
#     async with test_async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         print("Tables created!")
#
#     yield
#
#     async with test_async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         print("Tables dropped!")
#
#
#
# @pytest.mark.asyncio(loop_scope='session')
# async def test_root():
#     async with AsyncClient(
#             transport=ASGITransport(app=app), base_url="http://test"
#     ) as ac:
#         response = await ac.get("/")  # Adjust this path as necessary
#         assert response.status_code == 200
#
#
# @pytest.mark.asyncio(loop_scope='session')
# async def test_registration_and_login(setup_database):
#     await register_user()
#     await login()
#     await about_me()
#
#
# @pytest.mark.asyncio(loop_scope='session')
# async def test_list_users():
#     async with AsyncClient(
#             transport=ASGITransport(app=app), base_url="http://test"
#     ) as ac:
#         response = await ac.get("/v1/users/")  # Adjust this path as necessary
#         assert response.status_code == 200
#         assert len(response.json()) == 1
#
