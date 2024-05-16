from django import template

register = template.Library()
# using the @register decorator to register our custom template filter
# check out django doc
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity