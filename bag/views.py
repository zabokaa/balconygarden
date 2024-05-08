from django.shortcuts import render

# Views
def view_bag(request):
    """" A view to return the bag content page """
    return render(request, 'bag/bag.html')