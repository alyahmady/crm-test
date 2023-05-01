from django.contrib import admin

from car_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "tag",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_filter = ("is_active",)
    ordering = (
        "-is_active",
        "-updated_at",
        "-created_at",
    )
    search_fields = ("tag", "name")
