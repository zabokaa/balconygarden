rom django.shortcuts import render
from .models import Product

# Views
def index(request):
    """" A view to return the index page of products, 
    including sorting and search queries"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
