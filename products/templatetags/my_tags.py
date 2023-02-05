from django import template
from django.db.models import Sum
from ..models import WishlistModel, ProductModel

register = template.Library()

@register.simple_tag
def is_cart(request, id):
    cart = request.session.get('cart', [])
    return id in cart


@register.simple_tag
def cart_info(request):
    cart = request.session.get('cart', [])
    qs = ProductModel.get_cart_objects(cart)
    if not qs:
        price = 0.0
    else:
        price = qs.aggregate(Sum('real_price'))['real_price__sum']
    return len(cart), price

@register.simple_tag
def get_current_price(request, x):
    data = request.GET.get('price')
    if data:
        return data.split(';')[x]
    else:
        return 'null'
    
@register.filter
def is_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()