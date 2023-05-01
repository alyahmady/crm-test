import mimetypes
from pathlib import Path

import environ

from .env import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = env.bool("DEBUG", None)

if DEBUG is None:
    environ.Env.read_env(BASE_DIR / "deploy" / "environments", "django.env")
    DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env.str("SECRET_KEY")

ROOT_URLCONF = "crmtest.urls"

WSGI_APPLICATION = "crmtest.wsgi.application"

LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en-us")
TIME_ZONE = env.str("TIMEZONE", default="UTC")

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user_app.CustomUser"

mimetypes.add_type("application/javascript", ".js", True)
