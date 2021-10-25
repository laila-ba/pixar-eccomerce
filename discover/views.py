from django.shortcuts import render

# Create your views here.

def all_films(request):
    """ A view that renders the films contents page """
    return render(request, 'discover/films.html')

def film_templates(request):
        return render(request, 'discover/luca.html')

def all_shorts(request):
    """ A view that renders the shorts contents page """
    return render(request, 'discover/shorts.html')

def short_templates(request):
        return render(request, 'discover/bao.html')