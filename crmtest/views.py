import logging

from django.conf import settings
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import render
from redis import Redis
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from crmtest.settings import UserRole

logger = logging.getLogger(settings.LOGGER_NAME)


def home_view(request: HttpRequest):
    user = request.user

    if user.is_authenticated and user.is_active:
        is_staff = user.groups.filter(name=UserRole.STAFF.value).exists()
        if is_staff:
            return render(request, "home/staff.html", {"user": request.user})

        is_admin = user.groups.filter(name=UserRole.ADMIN.value).exists()
        if is_admin:
            return render(request, "home/admin.html", {"user": request.user})

        return render(request, "home/authenticated.html", {"user": request.user})

    else:
        return render(request, "home/anonymous.html")


@api_view(["GET"])
@permission_classes([AllowAny])
def perform_healthcheck(request):
    status_code = 200
    is_database_working = True
    is_redis_working = True

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
    except Exception as exc:
        logger.exception("Error in health check", exc_info=exc)
        is_database_working = False
        status_code = 400

    try:
        if settings.REDIS_PASSWORD:
            redis_conn = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD,
                socket_connect_timeout=1,
            )
        else:
            redis_conn = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                socket_connect_timeout=1,
            )
        redis_conn.ping()
    except Exception as exc:
        logger.exception("Error in health check", exc_info=exc)
        is_redis_working = False
        status_code = 400

    return Response(
        data={
            "healthcheck": "Running",
            "is_database_working": is_database_working,
            "is_redis_working": is_redis_working,
        },
        status=status_code,
    )
