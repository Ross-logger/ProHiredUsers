from contextlib import asynccontextmanager
from typing import List

import httpx
from fastapi import FastAPI, HTTPException, Cookie, Request, Response, Depends
from fastapi_users import FastAPIUsers
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from redis import asyncio as aioredis

import src.base_config as auth_base_config
from src import utils, schemas
from src.database.database import create_db_and_tables, get_async_session
from src.database.manager import get_user_manager
from src.models.models import User
from src.schemas import UserRead, UserCreate
from src.database import crud

# Configuration imports
from config import HOST, PORT
from src.utils import get_user_id_from_cookies

VACANCY_SERVICE_URL = f'http://{HOST}:{2005}'

ok_status_codes = [
    200,  # OK
    201,  # Created
    202,  # Accepted
    204,  # No Content
    205,  # Reset Content
    206   # Partial Content
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

app = FastAPI(title="ProHired", lifespan=lifespan)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_base_config.auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_base_config.auth_backend),
    prefix="/v1/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/v1/auth",
    tags=["auth"],
)

@app.get("/", tags=["home"])
async def root():
    return {"message": "Welcome to ProHired!"}

@app.delete("/v1/users/", tags=["users"])
async def delete_user(response: Response, db: AsyncSession = Depends(get_async_session),
                      user_id: int = Depends(utils.get_user_id_from_cookies)):
    await crud.delete_self_user(db, user_id)
    response.delete_cookie(key="usersAuth")
    return {"message": "User and their vacancies deleted successfully."}

@app.get("/v1/users/me", response_model=schemas.UserRead, tags=["users"])
async def about_me(db: AsyncSession = Depends(get_async_session),
                   user_id: int = Depends(utils.get_user_id_from_cookies)):
    return await crud.get_user_by_id(db, user_id)

@app.get("/v1/users/", response_model=List[UserRead], tags=["users"])
async def list_users(db: AsyncSession = Depends(get_async_session), limit: int = 100):
    users = await crud.list_users(db, limit)
    return users

@app.post("/v1/vacancies/", tags=["vacancies"])
async def create_vacancy(
        new_vacancy_data: schemas.VacancyCreate,
        request: Request,
):
    jwt_token = request.cookies.get("usersAuth")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            VACANCY_SERVICE_URL + '/v1/vacancies/',
            json=new_vacancy_data.dict(),
            headers={"usersAuth": f"{jwt_token}"}
        )
        if response.status_code not in ok_status_codes:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@app.get("/v1/vacancies/", tags=["vacancies"])
async def list_vacancies(limit: int = 100):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            VACANCY_SERVICE_URL + '/v1/vacancies/',
            params={'limit': limit}
        )
        if response.status_code not in ok_status_codes:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@app.get("/v1/vacancies/{vacancy_id}", tags=["vacancies"])
@cache(expire=30)
async def get_vacancy(vacancy_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            VACANCY_SERVICE_URL + f'/v1/vacancies/{vacancy_id}'
        )
        if response.status_code not in ok_status_codes:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@app.delete("/v1/vacancies/{vacancy_id}", tags=["vacancies"])
async def delete_vacancy(vacancy_id: int, user_id=Depends(get_user_id_from_cookies)):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            VACANCY_SERVICE_URL + f'/v1/vacancies/{vacancy_id}',
            headers={"user_id": str(user_id)}
        )
        if response.status_code not in ok_status_codes:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return {"message": "Vacancy deleted successfully."}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host=HOST, port=int(PORT), reload=True)