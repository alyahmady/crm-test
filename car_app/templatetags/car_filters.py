from django import template

from car_app.models import Car

register = template.Library()


@register.filter(is_safe=True)
def choice_label(value: int):
    if value in Car.BodyStyle:
        return Car.BodyStyle(value).label
    return value
