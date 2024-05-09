from django.shortcuts import render, redirect

# Views
def view_bag(request):
    """" A view to return the bag content page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
# adding quantity and trasnform it to int as it is a string
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # storing the bag in the session and get the bag if it exists
    bag = request.session.get('bag', {})
# of theres exists already an item in the session 
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
    