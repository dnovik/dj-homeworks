from django import template


register = template.Library()


@register.filter
def replace_empty(value):
    if not value:
        field = '-'
    else:
        field = value
    return field


@register.filter
def replace_bool(value):
    if value is True:
        field = 'Да'
    elif value is False:
        field = 'Нет'
    else:
        field = value
    return field
