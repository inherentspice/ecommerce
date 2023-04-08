from django.shortcuts import render
from store.models import Product

def store(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'store/store.html', context)
