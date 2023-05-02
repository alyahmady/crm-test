from django.contrib.auth.models import AbstractUser
from django.db import models

from crmtest.settings import BodyStyle


class Car(models.Model):
    # Info
    name = models.CharField(max_length=100)
    plate = models.CharField(max_length=50, unique=True, db_index=True)
    body_style = models.PositiveSmallIntegerField(
        choices=BodyStyle.choices, default=BodyStyle.OTHER
    )

    # Date time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Flags
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.plate})"

    class Meta:
        app_label = "car_app"
        db_table = "crmtest_cars"
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ("-created_at",)
