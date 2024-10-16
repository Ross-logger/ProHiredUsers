import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


class RedisConfig:
    BROKER_URL = REDIS_URL
