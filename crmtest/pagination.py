import math

from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    max_limit = settings.PAGINATION_MAX_PAGE_SIZE

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "data_count": self.count,
                "page_count": math.ceil(self.count / self.limit),
                "result": data,
            }
        )
