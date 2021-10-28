from django.shortcuts import render

# Create your views here.

def all_films(request):
    """ A view that renders the films contents page """
    return render(request, 'discover/films.html')

def luca(request):
        return render(request, 'discover/luca.html')

def soul(request):
        return render(request, 'discover/soul.html')

def onward(request):
        return render(request, 'discover/onward.html')

def toy4(request):
        return render(request, 'discover/toy4.html')

def i2(request):
        return render(request, 'discover/i2.html')

def coco(request):
        return render(request, 'discover/coco.html')

def cars3(request):
        return render(request, 'discover/cars3.html')

def dory(request):
        return render(request, 'discover/dory.html')

def dino(request):
        return render(request, 'discover/dino.html')

def io(request):
        return render(request, 'discover/io.html')

def mu(request):
        return render(request, 'discover/mu.html')

def brave(request):
        return render(request, 'discover/brave.html')

def cars2(request):
        return render(request, 'discover/cars2.html')

def toy3(request):
        return render(request, 'discover/toy3.html')

def up(request):
        return render(request, 'discover/up.html')

def walle(request):
        return render(request, 'discover/walle.html')

def rat(request):
        return render(request, 'discover/rat.html')

def cars(request):
        return render(request, 'discover/cars.html')

def incredibles(request):
        return render(request, 'discover/incredibles.html')

def nemo(request):
        return render(request, 'discover/nemo.html')

def monsters(request):
        return render(request, 'discover/monsters.html')

def toy2(request):
        return render(request, 'discover/toy2.html')

def bug(request):
        return render(request, 'discover/bug.html')

def toy1(request):
        return render(request, 'discover/toy1.html')

def all_shorts(request):
    """ A view that renders the shorts contents page """
    return render(request, 'discover/shorts.html')

def short_templates(request):
        return render(request, 'discover/bao.html')