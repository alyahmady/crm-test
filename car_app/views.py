from django.db.models import OuterRef, Exists
from django.shortcuts import render

from car_app.models import Car
from crmtest.auth import active_user_required
from rental_app.models import Rental


@active_user_required
def car_list_view(request):
    in_progress_rental = Rental.objects.filter(car_id=OuterRef("pk"), is_returned=False)
    cars = Car.objects.annotate(is_available=~Exists(in_progress_rental)).values(
        "id", "name", "plate", "is_available"
    )

    return render(request, "car_app/car_list.html", {"cars": cars})
