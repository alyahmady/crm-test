from pathlib import Path

from .env import env
from .logging import LOGS_DIRECTORY

EMAIL_HOST = env.str("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", 587)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", None)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", False)
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", "info@crmtest.org")

EMAIL_FOLDER_NAME = env.str("EMAIL_FOLDER_NAME", "emails")
EMAIL_FILE_PATH = (LOGS_DIRECTORY / EMAIL_FOLDER_NAME).resolve()

EMAIL_BACKEND = env.str("EMAIL_BACKEND", "console")

if EMAIL_BACKEND == "console":
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
elif EMAIL_BACKEND == "file":
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    Path(EMAIL_FILE_PATH).mkdir(parents=True, exist_ok=True)
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
