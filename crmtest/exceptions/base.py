import logging
import uuid

from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

logger = logging.getLogger(settings.LOGGER_NAME)


class CustomException(APIException):
    default_error_message = "INTERNAL_SERVER_ERROR"
    default_status_code = HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self,
        error_message: str = None,
        error_data: dict | list | str = None,
        status_code: int = None,
        log_error: bool = False,
        log_exception: Exception | bool = None,
        **kwargs,
    ):
        self.error_message = error_message or self.default_error_message
        self.status_code = status_code or self.default_status_code

        if log_error:
            error_id = str(uuid.uuid4())
            log_message = f"ID -> {error_id} - Message -> {self.error_message}"

            if log_exception is True or isinstance(log_exception, Exception):
                logger.exception(msg=log_message, exc_info=log_exception)
            else:
                logger.error(msg=log_message)

            match error_data:
                case dict():
                    error_data["error_id"] = error_id
                case list():
                    error_data.append({"error_id": error_id})
                case str():
                    error_data += f"ErrorID: {error_id}"
                case None:
                    error_data = {"error_id": error_id}

        self.error_data = error_data

        self.auth_header = kwargs.get("auth_header", "")
        self.wait = kwargs.get("wait", "")

        super().__init__(**kwargs)

    def __str__(self):
        return self.error_message or ""
