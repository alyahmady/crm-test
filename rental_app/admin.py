from django.contrib import admin

from rental_app.models import Rental



@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "car",
        "started_at",
        "expire_at",
        "is_returned",
    )
    list_filter = ("is_returned",)
    ordering = (
        "-is_returned",
        "-started_at",
        "-expire_at",
    )
    search_fields = (
        "user__email",
        "car__plate",
        "car__name",
        "user__last_name",
        "user__first_name",
    )
