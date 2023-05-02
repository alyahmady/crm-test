import enum

from django.db import models


class UserRole(enum.StrEnum):
    STAFF = "staff"
    ADMIN = "admin"


class BodyStyle(models.IntegerChoices):
    SEDAN = 1, "Sedan"
    SUV = 2, "SUV"
    HATCHBACK = 3, "Hatchback"
    PICKUP = 4, "Pickup"
    VAN = 5, "Van"
    TRUCK = 6, "Truck"
    BUS = 7, "Bus"
    MOTORCYCLE = 8, "Motorcycle"
    TRICYCLE = 9, "Tricycle"
    BICYCLE = 10, "Bicycle"
    OTHER = 11, "Other"
