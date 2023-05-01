from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
    HTTP_403_FORBIDDEN,
    HTTP_400_BAD_REQUEST,
    HTTP_429_TOO_MANY_REQUESTS,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from .base import (
    CustomException,
)


class DatabaseException(CustomException):
    default_error_message = "Database error"
    default_status_code = HTTP_500_INTERNAL_SERVER_ERROR


class DataInvalidException(CustomException):
    default_error_message = "Invalid data"
    default_status_code = HTTP_400_BAD_REQUEST


class LimitException(CustomException):
    default_error_message = "Limit reached"
    default_status_code = HTTP_429_TOO_MANY_REQUESTS


class NotFoundException(CustomException):
    default_error_message = "Not found"
    default_status_code = HTTP_404_NOT_FOUND


class DuplicateException(CustomException):
    default_error_message = "Duplicate entity found"
    default_status_code = HTTP_409_CONFLICT


class AuthorizationException(CustomException):
    default_error_message = "Authorization Error"
    default_status_code = HTTP_403_FORBIDDEN
