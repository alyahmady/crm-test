from django.contrib import admin

from car_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "plate",
        "body_style",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_filter = ("is_active", "body_style")
    ordering = (
        "-is_active",
        "-updated_at",
        "-created_at",
    )
    search_fields = ("plate", "name")
