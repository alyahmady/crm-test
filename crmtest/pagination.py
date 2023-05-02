import math
from typing import Tuple

from django.conf import settings
from django.db.models import QuerySet
from django.http import HttpRequest
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


def get_pagination_query_params(request: HttpRequest) -> Tuple[int, int]:
    limit = int(request.GET.get("limit", settings.PAGINATION_PAGE_SIZE))
    offset = int(request.GET.get("offset", 0))
    return limit, offset


def get_pagination_detail(queryset_count: int | QuerySet, limit, offset):
    if isinstance(queryset_count, QuerySet):
        queryset_count = queryset_count.count()

    return {
        "pages_count": queryset_count // limit + (1 if queryset_count % limit else 0),
        "current_page": offset // limit + 1,
        "next_offset": offset + limit if offset + limit < queryset_count else None,
        "previous_offset": offset - limit if offset - limit >= 0 else None,
    }


def paginate_queryset(queryset: QuerySet, limit: int, offset: int) -> Tuple[int, int]:
    queryset_count = queryset.count()
    paginated_queryset = queryset[offset : offset + limit]

    return paginated_queryset, queryset_count
