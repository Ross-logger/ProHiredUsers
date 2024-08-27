from src.celery_tasks.redis_config import RedisConfig


class CeleryConfig:
    broker_url = RedisConfig.BROKER_URL
    timezone = 'UTC'
    beat_schedule = {
        'send-daily-report': {
            'task': 'src.celery_tasks.tasks.send_report',
            'schedule': 20,  # 24 hours in seconds
        },
    }
