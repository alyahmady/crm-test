from pathlib import Path

from .base import BASE_DIR
from .env import env

STATIC_URL = "/static/"
STATIC_ROOT = env.str("STATIC_ROOT", BASE_DIR / "static")

STATICFILES_DIRS = [BASE_DIR / "staticfiles"]
for directory in STATICFILES_DIRS:
    Path(directory).mkdir(parents=True, exist_ok=True)

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_ROOT = env.str("MEDIA_ROOT", BASE_DIR / "media")
MEDIA_URL = "/media/"
