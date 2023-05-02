from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    # Info
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)

    # Identifier
    email = models.EmailField(unique=True, max_length=255)
    username = None

    # Date time
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Auditing
    last_login_info = models.JSONField(null=True, default=dict)

    # Flags
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name.strip()} {self.last_name.strip()}"
        return None

    def __str__(self) -> str:
        if self.full_name:
            return f"{self.full_name}: {self.email}"
        return f"{self.email}"

    class Meta:
        app_label = "user_app"
        db_table = "crmtest_users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-date_joined",)
