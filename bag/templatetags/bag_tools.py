from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate the subtotal of a product """
    return price * quantity
