from dotenv import load_dotenv

import os

load_dotenv()

VACANCY_SERVICE_URL = os.getenv("VACANCY_SERVICE_URL") or "http://vacancies_service:8005"

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

TEST_DB_HOST = os.environ.get("TEST_DB_HOST")
TEST_DB_PORT = os.environ.get("TEST_DB_PORT")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME")
TEST_DB_USER = os.environ.get("TEST_DB_USER")
TEST_DB_PASS = os.environ.get("TEST_DB_PASS")

JWT_SECRET = os.environ.get("JWT_SECRET")

ok_status_codes = [
    200,  # OK
    201,  # Created
    202,  # Accepted
    204,  # No Content
    205,  # Reset Content
    206  # Partial Content
]
