from django.shortcuts import render

# Create your views here.

def all_films(request):
    """ A view that renders the bag contents page """

    return render(request, 'discover/films.html')

def all_shorts(request):
    """ A view that renders the bag contents page """

    return render(request, 'discover/shorts.html')