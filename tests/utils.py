from httpx import AsyncClient
from httpx import ASGITransport
from src.main import app


async def register_user() -> None:
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/v1/auth/register", json={
            "email": "string",
            "password": "string",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string",
            "phone_number": "string"
        })
        print("REGISTER RESPONSE:", response.json())
    assert response.status_code == 201


async def login() -> str:
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post("/v1/auth/jwt/login", data={
            "username": "string",
            "password": "string"
        })
        print("LOGIN RESPONSE:", response.cookies)
        assert response.status_code == 204
        jwt_token = response.cookies.get('usersAuth')
        print("JWT TOKEN:", jwt_token)
        return jwt_token


async def about_me() -> None:
    jwt_token = await login()
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test", cookies={"usersAuth": jwt_token}
    ) as ac:
        response = await ac.get(
            "/v1/users/me",
        )
        print("ABOUT ME RESPONSE:", response.json())
    assert response.status_code == 200
