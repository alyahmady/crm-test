from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.shortcuts import render, redirect

from crmtest.auth import admin_or_staff_required, staff_required
from crmtest.pagination import (
    get_pagination_query_params,
    get_pagination_detail,
    paginate_queryset,
)
from .forms import RentalForm
from .models import Rental


@admin_or_staff_required
def rental_list_view(request):
    limit, offset = get_pagination_query_params(request)

    rentals_queryset = (
        Rental.objects.select_related("user", "car")
        .annotate(
            car_name=F("car__name"),
            car_plate=F("car__plate"),
            user_full_name=Concat(
                F("user__first_name"),
                Value(" "),
                F("user__last_name"),
                output_field=CharField(),
            ),
            user_email=F("user__email"),
        )
        .values(
            "id",
            "car_name",
            "car_plate",
            "user_full_name",
            "user_email",
            "started_at",
            "expire_at",
        )
    )

    paginated_rentals, rentals_count = paginate_queryset(
        rentals_queryset, limit, offset
    )
    pagination = get_pagination_detail(rentals_count, limit, offset)

    return render(
        request,
        "rental_app/rental_list.html",
        {
            "rentals": paginated_rentals,
            "rentals_count": rentals_count,
            "limit": limit,
            "pagination": pagination,
        },
    )


@staff_required
def create_rental_view(request):
    if request.method == "POST":
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rental_app:rental-list")
    else:
        form = RentalForm()

    return render(request, "rental_app/create_rental.html", {"form": form})
