from django.shortcuts import render

# Create your views here.

def all_films(request):
    """ A view that renders the films contents page """
    return render(request, 'discover/films.html')

def film_templates(request):
        return render(request, 'discover/luca.html'),
        return render(request, 'discover/soul.html'),
        return render(request, 'discover/onward.html'),
        return render(request, 'discover/toy4.html'),
        return render(request, 'discover/i2.html'),
        return render(request, 'discover/coco.html'),
        return render(request, 'discover/cars3.html'),
        return render(request, 'discover/dory.html'),
        return render(request, 'discover/dino.html'),
        return render(request, 'discover/io.html'),
        return render(request, 'discover/mu.html'),
        return render(request, 'discover/brave.html'),
        return render(request, 'discover/cars2.html'),
        return render(request, 'discover/toy3.html'),
        return render(request, 'discover/up.html'),
        return render(request, 'discover/walle.html'),
        return render(request, 'discover/rat.html'),
        return render(request, 'discover/cars.html'),
        return render(request, 'discover/incredibles.html'),
        return render(request, 'discover/nemo.html'),
        return render(request, 'discover/monsters.html'),
        return render(request, 'discover/toy2.html'),
        return render(request, 'discover/bug.html'),
        return render(request, 'discover/toy1.html'),

def all_shorts(request):
    """ A view that renders the shorts contents page """
    return render(request, 'discover/shorts.html')

def short_templates(request):
        return render(request, 'discover/bao.html')