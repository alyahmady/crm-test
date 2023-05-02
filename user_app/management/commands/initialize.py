import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


# Run this file using "python manage.py initialize" command


class Command(BaseCommand):
    help = "Create SuperUser (admin)"

    def handle(self, *args, **options):
        CustomUser = get_user_model()

        superuser_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        superuser_password = os.getenv("DJANGO_SUPERUSER_PASS")
        if superuser_email and superuser_password:
            superuser, _ = CustomUser.objects.get_or_create(email=superuser_email)

            staff_group = Group.objects.get(name__iexact="staff")
            admin_group = Group.objects.get(name__iexact="admin")
            staff_group.user_set.add(superuser)
            admin_group.user_set.add(superuser)

            superuser.is_staff = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.set_password(superuser_password)
            superuser.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"SuperUser for {superuser_email} is created successfully"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("ENV Variables are not set to create SuperUser")
            )
