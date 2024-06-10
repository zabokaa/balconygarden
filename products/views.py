from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from cloudinary.models import CloudinaryField
from .models import Product, Category, Inventory
from .forms import ProductForm, InventoryForm

# Views
def all_products(request):
    """" A view to return the index page of products, 
    including sorting and search queries"""
    products = Product.objects.all()
        # If the key does not exist, None is returned
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # print(request.GET) #debugging
        if 'sort' in request.GET:
            # sortkey is the key that we are sorting by
            sortkey = request.GET['sort']
            # if the key is name, we are sorting by name
            # creating sortkey so we do not changing the original name variable
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                # using lower built-in fct to make the sorting case-insensitive
                products = products.annotate(lower_name=Lower('name'))
            # if the key is category, we are sorting by category
            if sortkey == 'category':
                sortkey = 'category__name' #double underscore syntax allows us to drill into a related model
            # if the key is direction, we are sorting by direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                # if the direction is descending, we are adding a minus sign in front of the sortkey
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # sorting the products by the sortkey with order-by method
            products = products.order_by(sortkey)
        if 'category' in request.GET:    
            categories = request.GET['category'].split(',')
            # print('categories:', categories) #debugging
            products = products.filter(category__name__in=categories)
            # converting list of strings in an acutal list of objects, so we can enter them in the filter
            categories = Category.objects.filter(name__in=categories)
            print('categories:', categories) #debugging

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
# return current sorting mehod to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """" A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    inventory = Inventory.objects.get(product=product)
    context = {
        'product': product,
        'inventory': inventory,
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # save the form to the database
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def inventory_management(request):
    """ View for the superuser to manage inventory """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query))
    else:
        products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/inventory_management.html', context)

@login_required
def update_inventory(request, product_id):
    """ Update the inventory of a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    inventory = get_object_or_404(Inventory, product=product)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated inventory!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update inventory. Please ensure the form is valid.')
    else:
        form = InventoryForm(instance=inventory)
        messages.info(request, f'You are updating the inventory for {product.name}')

    template = 'products/update_inventory.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)