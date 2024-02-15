from django import template

register=template.Library()

@register.simple_tag(name='total')
def total(cart):
    i=0
    for item in cart.added_item.all():
        i+=item.quantity*item.product.price
    return i
        
    