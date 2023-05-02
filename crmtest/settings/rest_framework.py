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
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day",
        "user": "1000/day",
        "default_throttle_rate": "5/min",
        "create_car_rate": "6/min",
        "retrieve_car_rate": "35/min",
        "list_car_rate": "30/min",
        "update_car_rate": "10/min",
        "destroy_car_rate": "6/min",
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "crmtest.exceptions.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "crmtest.pagination.CustomLimitOffsetPagination",
    "PAGE_SIZE": PAGINATION_PAGE_SIZE,
}

API_VERSION = env.str("API_VERSION", "v1")
PREFIX = env.str("API_PREFIX", "api")
API_PREFIX = f"{PREFIX}/{API_VERSION}"
