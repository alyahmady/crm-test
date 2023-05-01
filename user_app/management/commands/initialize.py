import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


# Run this file using "python manage.py initialize" command


class Command(BaseCommand):
    help = "Create SuperUser (admin)"

    def handle(self, *args, **options):
        User = get_user_model()

        admin_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        admin_password = os.getenv("DJANGO_SUPERUSER_PASS")
        if admin_email and admin_password:
            admin, _ = User.objects.get_or_create(email=admin_email)
            admin.is_staff = True
            admin.is_superuser = True
            admin.is_active = True
            admin.set_password(admin_password)
            admin.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"SuperUser for {admin_email} with {admin_password} is created successfully"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("ENV Variables are not set to create SuperUser")
            )
