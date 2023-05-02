from rest_framework import status

from .base import CustomResponse


class CreateResponse(CustomResponse):
    def __init__(
        self, data: dict | None = None, status=status.HTTP_201_CREATED, *args, **kwargs
    ):
        super().__init__(data=data, status=status, *args, **kwargs)


class ListResponse(CustomResponse):
    def __init__(self, data: list, status=status.HTTP_200_OK, *args, **kwargs):
        super().__init__(data=data, status=status, *args, **kwargs)


class RetrieveResponse(CustomResponse):
    def __init__(self, data: dict, status=status.HTTP_200_OK, *args, **kwargs):
        super().__init__(data=data, status=status, *args, **kwargs)


class UpdateResponse(CustomResponse):
    def __init__(self, data: dict | list, status=status.HTTP_200_OK, *args, **kwargs):
        super().__init__(data=data, status=status, *args, **kwargs)


class DeleteResponse(CustomResponse):
    def __init__(self, status=status.HTTP_204_NO_CONTENT, *args, **kwargs):
        super().__init__(status=status, *args, **kwargs)
