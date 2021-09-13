from .views import  _cart_id
from .models import Cart,CartItem

def counter(request):
    cart_count=0
    try:
     cart=Cart.objects.filter(cart_id=_cart_id(request))
     cart_items=CartItem.objects.all().filter(cart=cart[:1])
    except cart_items.DoesNotExist:
      cart_count=0

    for cart_item in cart_items:
        cart_count+=cart_item.quantity

    return dict(cart_count=cart_count)
