import logging
import uuid

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from response import ErrorResponse
from .base import CustomException

logger = logging.getLogger(settings.LOGGER_NAME)


def custom_exception_handler(exc: Exception, context: dict):
    if isinstance(exc, CustomException):
        headers = {}
        if exc.auth_header:
            headers["WWW-Authenticate"] = exc.auth_header
        if exc.wait and exc.wait.isdigit():
            headers["Retry-After"] = str(exc.wait)

        return ErrorResponse(
            message=exc.error_message,
            data=exc.error_data,
            status=exc.status_code,
            headers=headers,
        )

    response: Response | None = exception_handler(exc, context)
    response_data = getattr(response, "data", None)

    error_id = str(uuid.uuid4())
    if isinstance(response, Response):
        if response.status_code in range(200, 499):
            logger.error(f"ID -> {error_id} - Data -> {response_data}")
        else:
            logger.exception(
                f"ID -> {error_id} - Data -> {response_data}", exc_info=exc
            )

        match response_data:
            case dict():
                response_data["error_id"] = error_id
            case list():
                response_data.append({"error_id": error_id})
            case str():
                response_data += f"ErrorID: {error_id}"
            case None:
                response_data = {"error_id": error_id}

        return ErrorResponse(
            message="Error",
            data=response_data,
            status=response.status_code,
            headers=response.headers,
        )

    logger.exception(f"ID: {error_id}", exc_info=exc)
    return ErrorResponse(
        message="Unknown error",
        data={"error_id": error_id},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
