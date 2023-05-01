from django.contrib.auth.models import AbstractUser
from django.db import models


class Rental(models.Model):
    # Relations
    user = models.ForeignKey(
        "user_app.CustomUser",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
        related_name="rentals",
    )
    car = models.ForeignKey(
        "car_app.Car",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
        related_name="rentals",
    )

    # Date time
    started_at = models.DateTimeField(null=False)
    expire_at = models.DateTimeField(null=False)

    # Flags
    is_returned = models.BooleanField(default=False)

    def __str__(self) -> str:
        user = self.user.full_name or self.user.email
        car = str(self.car)
        return f"{user} - {car}"

    class Meta:
        app_label = "rental_app"
        db_table = "crmtest_rentals"
        verbose_name = "Rental"
        verbose_name_plural = "Rental"
        ordering = ("-started_at", "-expire_at")
