from django.shortcuts import render, redirect
from carts.models import CartItem

def place_order(request):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
