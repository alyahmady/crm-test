from .env import env

PAGINATION_MAX_PAGE_SIZE = env.int("PAGINATION_MAX_PAGE_SIZE", default=50)
PAGINATION_PAGE_SIZE = env.int("PAGINATION_PAGE_SIZE", default=10)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "login": "3/min",
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "crmtest.exceptions.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "crmtest.pagination.CustomLimitOffsetPagination",
    "PAGE_SIZE": PAGINATION_PAGE_SIZE,
}
