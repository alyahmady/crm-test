from django.conf import settings
from django.db.models import Exists, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from car_app.api.v1.filters import CarListFilterSet
from car_app.api.v1.serializers import CarSerializer
from car_app.models import Car
from crmtest.permissions import IsActiveAdmin
from rental_app.models import Rental


class CarViewSet(ModelViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer
    permission_classes = [IsActiveAdmin]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
    )
    search_fields = ["name", "=plate"]
    filterset_class = CarListFilterSet

    def get_queryset(self):
        in_progress_rental = Rental.objects.filter(
            car_id=OuterRef("pk"), is_returned=False
        )
        return Car.objects.filter(is_active=True).annotate(
            is_available=~Exists(in_progress_rental)
        )

    def get_throttles(self):
        action = self.action.lower()

        match action:
            case "create":
                self.throttle_scope = "create_car_rate"
            case "retrieve":
                self.throttle_scope = "retrieve_car_rate"
            case "list":
                self.throttle_scope = "list_car_rate"
            case "update":
                self.throttle_scope = "update_car_rate"
            case "destroy":
                self.throttle_scope = "destroy_car_rate"
            case _:
                self.throttle_scope = "default_throttle_rate"

        return super(CarViewSet, self).get_throttles()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Search through Car names or exact plate number.",
                required=False,
            ),
            OpenApiParameter(
                name="limit",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description=f"Number of results to return per page. Default to {settings.PAGINATION_PAGE_SIZE}",
                required=False,
            ),
            OpenApiParameter(
                name="offset",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="The initial index from which to return the results. Default to 0",
                required=False,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(methods=["PUT"], exclude=True)
    def put(self, request):
        # As updating a car plate number is not logical, but it can not be null and duplicate,
        #  I think we don't need idempotency for updating this entity (Car).
        raise MethodNotAllowed("PUT")

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance: Car):
        instance.is_active = False
        instance.save(force_update=True, update_fields=["is_active"])
