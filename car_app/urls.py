from django.urls import path

from car_app.views import car_list_view

app_name = "car_app"

urlpatterns = [
    path("list/", car_list_view, name="car-list"),
]
