from typing import AsyncGenerator
import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# Connect to the 'postgres' database to create the database if it doesn't exist
POSTGRES_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/postgres"
TARGET_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(TARGET_DATABASE_URL, echo=False)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_db_if_not_exists():
    """Create the target database if it doesn't exist."""
    try:
        # Use asyncpg directly to connect to the 'postgres' default database
        conn = await asyncpg.connect(
            user=DB_USER, password=DB_PASS, database="postgres", host=DB_HOST, port=DB_PORT
        )

        # Check if the target database exists
        result = await conn.fetchval(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")

        if not result:
            print(f"Database '{DB_NAME}' does not exist, creating...")
            await conn.execute(f'CREATE DATABASE "{DB_NAME}"')
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        await conn.close()
    except Exception as e:
        print(f"Error while checking/creating database: {e}")
    finally:
        await conn.close()


async def create_db_and_tables():
    """Ensure the database and tables exist."""
    # Step 1: Ensure the database exists
    await create_db_if_not_exists()

    # Step 2: Create the tables within the target database
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    print("Tables created!")


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()