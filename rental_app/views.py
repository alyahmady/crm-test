from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.shortcuts import render, redirect

from crmtest.auth import admin_or_staff_required, staff_required
from .forms import RentalForm
from .models import Rental


@admin_or_staff_required
def rental_list_view(request):
    rentals = (
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

    return render(request, "rental_app/rental_list.html", {"rentals": rentals})


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
