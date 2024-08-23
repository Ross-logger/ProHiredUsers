from typing import Optional
from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    phone_number: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    phone_number: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class VacancyRead(BaseModel):
    title: str
    salary: str
    description: str
    user_id: int

    class Config:
        from_attributes = True


class VacancyCreate(BaseModel):
    title: str
    salary: str
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "title": "Software Engineer",
                "salary": "100000 USD",
                "description": "Develops software solutions."
            }
        }
