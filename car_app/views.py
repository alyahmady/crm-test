from django.db.models import OuterRef, Exists
from django.shortcuts import render

from car_app.models import Car
from crmtest.auth import active_user_required
from crmtest.pagination import (
    get_pagination_query_params,
    paginate_queryset,
    get_pagination_detail,
)
from rental_app.models import Rental


@active_user_required
def car_list_view(request):
    limit, offset = get_pagination_query_params(request)

    in_progress_rental = Rental.objects.filter(car_id=OuterRef("pk"), is_returned=False)
    cars_queryset = (
        Car.objects.filter(is_active=True)
        .annotate(is_available=~Exists(in_progress_rental))
        .values("name", "plate", "body_style", "is_available")
    )

    paginated_cars, cars_count = paginate_queryset(cars_queryset, limit, offset)
    pagination = get_pagination_detail(cars_count, limit, offset)

    return render(
        request,
        "car_app/car_list.html",
        {
            "cars": paginated_cars,
            "cars_count": cars_count,
            "limit": limit,
            "pagination": pagination,
        },
    )
