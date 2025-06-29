from django import template

register = template.Library()

@register.filter
def repeat(value, times):
    """Repeat a string value 'times' number of times"""
    try:
        return value * int(times)
    except (ValueError, TypeError):
        return ''

@register.filter
def subtract(value, arg):
    """Subtract arg from value"""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0
