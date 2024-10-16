import asyncio
from celery import Celery
from src.celery_tasks.celery_config import CeleryConfig
from src.database.database import get_async_session
from src.database import crud

celery_app = Celery('dashboard_service')
celery_app.config_from_object(CeleryConfig)


@celery_app.task(bind=True, max_retries=5)
def send_report(self):
    loop = asyncio.new_event_loop()
    return loop.run_until_complete(run_task_send_report(self))


# Mocking report while Vacancy Microservice is down
async def run_task_send_report(task):
    try:
        report = {
            "users": 8675,
            "vacancies": 903  # Hardcoded dummy value
        }
        print("REPORT:", report)
        return report
    except Exception as e:
        print("Error occurred while reporting via Celery:", e)
        raise task.retry(exc=e, countdown=5)



# async def run_task_send_report(task):
#     async for session in get_async_session():  # Use async for to get the session
#         try:
#             # Fetch user count from the database
#             user_count = await crud.get_users_count(session)
#
#             # Fetch vacancy count from the vacancy service
#             vacancy_count = await get_vacancies_count()
#
#             # Compile report
#             report = {
#                 "users": user_count,
#                 "vacancies": vacancy_count
#             }
#             print("REPORT:", report)
#             return report
#         except Exception as e:
#             print("Error occurred:", e)
#             raise task.retry(exc=e, countdown=5)
#
#
# async def get_vacancies_count():
#     async with httpx.AsyncClient() as client:
#         response = await client.get(VACANCY_SERVICE_URL + "/v1/vacancies/count")
#         response.raise_for_status()
#         return response.json()["count"]  # Adjust based on your API response structure

