import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


class CeleryConfigurations:
    timezone = settings.TIME_ZONE

    # SET WITH DEBUG TO NOT REPORT GRANULARITY IN PRODUCTION
    task_track_started = settings.DEBUG
    task_time_limit = 60  # seconds

    broker_url = settings.REDIS_CONNECTION_URI
    if settings.CACHE_ENGINE == "redis":
        result_backend = settings.REDIS_CONNECTION_URI
    else:
        result_backend = "db+sqlite:///celeryResults.db"

    task_routes = None
    task_queues = None
    task_create_missing_queues = True
    task_default_queue = "crmtest_celery"
    imports = [
        "rental_app.tasks"
    ]

    # Schedule tasks
    beat_schedule = {
        "alert-car-return": {
            "task": "rental_app.tasks.alert_car_return",
            "schedule": crontab(
                minute=f"*/{settings.CAR_RETURN_ALERT_INTERVAL_MINUTES}"
            ),
            "args": tuple(),
        },
    }


celery_app = Celery()
celery_app.config_from_object(CeleryConfigurations)
celery_app.autodiscover_tasks()
