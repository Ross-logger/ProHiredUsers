from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from src.database.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False, unique=True)
    username: str = Column(String, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    phone_number: str = Column(String)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
