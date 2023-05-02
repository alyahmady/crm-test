from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from django.template.loader import render_to_string
from django.utils import timezone

from crmtest.celery import celery_app
from rental_app.models import Rental

logger = get_task_logger(__name__)


@celery_app.task(ignore_result=False)
def alert_car_return() -> str:
    now = timezone.now()

    expired_rentals = (
        Rental.objects.filter(expire_at__gte=timezone.now(), is_returned=False)
        .select_related("user", "car")
        .annotate(
            car_name=F("car__name"),
            car_plate=F("car__plate"),
            car_body_style=F("car__body_style"),
            user_full_name=Concat(
                F("user__first_name"),
                Value(" "),
                F("user__last_name"),
                output_field=CharField(),
            ),
            user_email=F("user__email"),
            rental_started_at=F("started_at"),
            rental_expire_at=F("expire_at"),
        )
        .values(
            "car_name",
            "car_plate",
            "car_body_style",
            "user_full_name",
            "user_email",
            "started_at",
            "expire_at",
        )
        .iterator()
    )

    counter = 0
    error_counter = 0

    # Due to the need of `rental` as context for template,
    #  we need to iterate over the queryset instead of using `send_mass_mail`
    for rental in expired_rentals:
        html_message = render_to_string(
            template_name="rental_app/email/expired_rental.html",
            context={"rental": rental},
        )

        try:
            send_mail(
                subject="Reminder: Rental Car",
                message="Reminder: Return Your Rental Car",
                from_email="info@crmtest.org",
                recipient_list=[rental["user_email"]],
                fail_silently=False,
                html_message=html_message,
            )

        except Exception as exc:
            logger.exception(
                f"Failed to send email to {rental['user_email']}: {str(exc)}"
            )
            error_counter = error_counter + 1

        else:
            counter = counter + 1

    return (
        f"Rental return alerts sent in {now.isoformat()}. "
        f"Success {counter - error_counter}, Failed {error_counter}"
    )
