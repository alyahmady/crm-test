from collections import OrderedDict

from rest_framework.response import Response


class CustomResponse(Response):
    def __init__(
        self, *args, message=None, data=None, status=200, error_id=None, **kwargs
    ):
        # Filtering kwargs
        response_kwargs = (
            "data",
            "status",
            "template_name",
            "headers",
            "exception",
            "content_type",
        )
        kwargs = {key: value for key, value in kwargs.items() if key in response_kwargs}
        super().__init__(**kwargs)

        self.message = message
        self.status = status or self.status_code
        self.error_id = error_id

        self.data = OrderedDict(
            {
                "status": status,
                "message": message,
                "result": data,
                "error_id": error_id,
            }
        )

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.data
