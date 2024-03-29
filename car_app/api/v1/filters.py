from django.db.models import QuerySet
from django_filters.rest_framework import FilterSet, ChoiceFilter

from car_app.models import Car
from crmtest.settings import BodyStyle


class CarListFilterSet(FilterSet):
    bodyStyle = ChoiceFilter(
        method="filter_by_car_body_style",
        help_text="Filtering by body style of car",
        choices=BodyStyle.choices,
    )

    def filter_by_car_body_style(
        self, queryset: QuerySet, name: str, value: int | str | BodyStyle
    ):
        try:
            value = int(value)
        except ValueError:
            return queryset

        if value in BodyStyle:
            queryset = queryset.filter(body_style=value)

        return queryset

    class Meta:
        model = Car
        fields = ("bodyStyle",)
