from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product
from django.db.models import Q
from django.contrib import messages

# Views
def all_products(request):
    """" A view to return the index page of products, 
    including sorting and search queries"""
    products = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Q generates a query that matches any of the given parameters
            # __icontains is a field lookup that matches the given string, with i for case-insensitive
            # | is the or operator
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """" A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/products.html', context)
