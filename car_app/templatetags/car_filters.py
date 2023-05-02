from django import template

from crmtest.settings import BodyStyle

register = template.Library()


@register.filter(is_safe=True)
def choice_label(value: int):
    if value in BodyStyle:
        return BodyStyle(value).label
    return value
