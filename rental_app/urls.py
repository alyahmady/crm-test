from django.urls import path

from rental_app.views import rental_list_view, create_rental_view

app_name = "rental_app"

urlpatterns = [
    path("list/", rental_list_view, name="rental-list"),
    path('create/', create_rental_view, name='create-rental'),
]
