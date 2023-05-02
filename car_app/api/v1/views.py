from django.conf import settings
from django.db.models import Exists, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
    )
    search_fields = ["@name", "=plate"] if settings.DB_POSTGRES else ["name", "=plate"]
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

    def perform_destroy(self, instance: Car):
        instance.is_active = False
        instance.save(force_update=True, update_fields=["is_active"])
