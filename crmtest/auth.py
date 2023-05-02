from django.contrib.auth.decorators import user_passes_test

from crmtest.settings import UserRole


def active_user_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_active,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def staff_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name=UserRole.STAFF.value).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def admin_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(name=UserRole.ADMIN.value).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def admin_or_staff_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.groups.filter(
            name__in=(UserRole.ADMIN.value, UserRole.STAFF.value)
        ).exists(),
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
