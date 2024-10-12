import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")


class RedisConfig:
    BROKER_URL = REDIS_URL
