from .apps import INSTALLED_APPS
from .auth import AUTH_PASSWORD_VALIDATORS, LOGIN_URL, HAS_SUPERUSER_GOD_MODE
from .base import (
    BASE_DIR,
    DEBUG,
    SECRET_KEY,
    ROOT_URLCONF,
    WSGI_APPLICATION,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    DEFAULT_AUTO_FIELD,
    AUTH_USER_MODEL,
)
from .cache import CACHES, REDIS_CONNECTION_URI, CACHE_ENGINE
from .database import DATABASES
from .email import (
    EMAIL_BACKEND,
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD,
    EMAIL_USE_TLS,
    EMAIL_USE_SSL,
    DEFAULT_FROM_EMAIL,
    EMAIL_FILE_PATH,
)
from .enums import *
from .jwt import SIMPLE_JWT
from .logging import LOGGING, LOGGER_NAME
from .middleware import MIDDLEWARE
from .misc import CAR_RETURN_ALERT_INTERVAL_MINUTES
from .paths import (
    STATICFILES_DIRS,
    STATICFILES_FINDERS,
    STATIC_URL,
    STATIC_ROOT,
    MEDIA_URL,
    MEDIA_ROOT,
)
from .rest_framework import (
    REST_FRAMEWORK,
    PAGINATION_MAX_PAGE_SIZE,
    PAGINATION_PAGE_SIZE,
    API_VERSION,
    API_PREFIX,
)
from .swagger import SPECTACULAR_SETTINGS
from .template import TEMPLATES
