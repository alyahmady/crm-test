from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    # Info
    name = models.CharField(max_length=100)
    tag = models.CharField(
        max_length=50, help_text="Tag of the car", unique=True, db_index=True
    )

    # Date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Flags
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.tag})"

    class Meta:
        app_label = "car_app"
        db_table = "crmtest_cars"
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ("-created_at",)
