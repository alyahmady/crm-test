from rest_framework.permissions import IsAuthenticated

from crmtest.auth import has_super_user_god_mode
from crmtest.settings import UserRole


class IsActiveAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if has_super_user_god_mode(request.user):
            return True

        is_authenticated = super().has_permission(request, view)

        user = request.user
        if not (is_authenticated and user.is_active):
            return False

        try:
            is_admin = user.groups.filter(name=UserRole.ADMIN.value).exists()
        except AttributeError:
            return False

        return is_admin
