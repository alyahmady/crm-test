from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

from crmtest.settings import UserRole


def has_super_user_god_mode(user):
    if settings.HAS_SUPERUSER_GOD_MODE:
        is_superuser = getattr(user, "is_superuser", False)
        if is_superuser is True:
            return True

    return False


def active_user_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: has_super_user_god_mode(u) or u.is_authenticated and u.is_active,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def staff_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: has_super_user_god_mode(u)
        or u.groups.filter(name=UserRole.STAFF.value).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def admin_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: has_super_user_god_mode(u)
        or u.groups.filter(name=UserRole.ADMIN.value).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def admin_or_staff_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: has_super_user_god_mode(u)
        or u.groups.filter(
            name__in=(UserRole.ADMIN.value, UserRole.STAFF.value)
        ).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
