from django.shortcuts import render

# Views
def index(request):
    """" A view to return the index page """
    return render(request, 'home/index.html')
