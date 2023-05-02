from django.contrib import admin
from django.forms import ModelForm

from user_app.models import CustomUser


class UserAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["last_login_info"].required = False
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = (
        "full_name",
        "email",
        "is_active",
        "display_permissions",
        "display_groups",
    )
    list_filter = ("is_superuser", "is_staff", "is_active")
    ordering = ("date_joined", "updated_at", "last_login")
    search_fields = ("email", "last_name", "first_name")

    @admin.display(
        description="Groups",
    )
    def display_groups(self, obj: CustomUser):
        return ", ".join([group.name for group in obj.groups.all()])

    @admin.display(
        description="Permissions",
    )
    def display_permissions(self, obj: CustomUser):
        return ", ".join([permission.name for permission in obj.user_permissions.all()])
