from django import template

from ..models import User

register = template.Library()


@register.filter
def to_int(value):
    return int(value)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, False)


@register.filter
def get_username(uid):
    return User.objects.get(id=uid).user_name


@register.filter
def x20(rate):
    return rate * 20
