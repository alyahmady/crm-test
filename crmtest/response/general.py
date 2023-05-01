from rest_framework import status

from .base import CustomResponse


class SuccessResponse(CustomResponse):
    def __init__(
        self, message=None, data=None, status=status.HTTP_200_OK, *args, **kwargs
    ):
        super().__init__(message, data, status, *args, **kwargs)


class ErrorResponse(CustomResponse):
    def __init__(
        self,
        message=None,
        data=None,
        status=status.HTTP_400_BAD_REQUEST,
        *args,
        **kwargs
    ):
        super().__init__(message, data, status, *args, **kwargs)
