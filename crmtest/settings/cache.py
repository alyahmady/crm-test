from .env import env

CACHE_ENGINE = env.str("CACHE_ENGINE", "redis").lower()
REDIS_CONNECTION_URI = env.str("REDIS_CONNECTION_URI", None)

if CACHE_ENGINE == "redis":
    REDIS_USER = env.str("REDIS_USER", "default")
    REDIS_PASSWORD = env.str("REDIS_PASSWORD", "foobared")
    REDIS_HOST = env.str("REDIS_HOST", "localhost")
    REDIS_PORT = env.str("REDIS_PORT", "6379")

    REDIS_CONNECTION_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_CONNECTION_URI,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": False,
            },
            "KEY_PREFIX": "CRM_TEST",
            "VERSION": 1,
        }
    }

    if REDIS_PASSWORD:
        CACHES["default"]["OPTIONS"]["PASSWORD"] = REDIS_PASSWORD
        REDIS_CONNECTION_URI = (
            f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"
        )
        CACHES["default"]["LOCATION"] = REDIS_CONNECTION_URI

else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique-crm-test-snowflake"
        }
    }