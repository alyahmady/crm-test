import os
from pathlib import Path

from .base import BASE_DIR
from .env import env

LOGS_DIRECTORY = BASE_DIR / env.str("LOGS_DIRECTORY", "logs")
LOGS_DIRECTORY.mkdir(parents=False, exist_ok=True)

DJANGO_LOG_FILENAME = env.str(
    "DJANGO_LOG_FILENAME", "debug.log"
)
CELERY_LOG_FILENAME = env.str("CELERY_LOG_FILENAME", "celeryDebug.log")

DJANGO_DEBUG_LOG_FILE = LOGS_DIRECTORY / DJANGO_LOG_FILENAME
CELERY_DEBUG_LOG_FILE = LOGS_DIRECTORY / CELERY_LOG_FILENAME

for log_file in (DJANGO_DEBUG_LOG_FILE, CELERY_DEBUG_LOG_FILE):
    if not os.path.isfile(log_file):
        Path(log_file).touch()

LOGGER_NAME = "debugLogger"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "\n\nTime: {asctime}\nFile: {pathname}\nModule: {module}"
            "\nFunction: {funcName}\nDetails: {message}\nArgs: {args}\n",
            "style": "{",
        },
        "simple": {
            "format": "\n{levelname} {asctime} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        LOGGER_NAME: {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": DJANGO_DEBUG_LOG_FILE,
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 250,
        },
        "celery": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": CELERY_DEBUG_LOG_FILE,
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 250,
        },
    },
    "loggers": {
        LOGGER_NAME: {
            "handlers": [LOGGER_NAME, "console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "celery": {
            "handlers": ["celery", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}