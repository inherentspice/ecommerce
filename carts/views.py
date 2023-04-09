from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

def _get_card_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_get_card_id(request))
    except:
        cart = Cart.objects.create(cart_id=_get_card_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()

    return redirect('cart')


def cart(request):
    return render(request, 'store/cart.html')
