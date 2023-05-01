import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_future_date_time(value: datetime.datetime):
    if value.tzinfo is None:
        value = timezone.make_aware(value)

    now = timezone.now()
    if value <= now:
        raise ValidationError("Expire date time must be in the future")
