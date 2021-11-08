from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.all_films, name='films'),
    path('luca/', views.luca, name='luca'),
    path('soul/', views.soul, name='soul'),
    path('onward/', views.onward, name='onward'),
    path('toy4/', views.toy4, name='toy4'),
    path('i2/', views.i2, name='i2'),
    path('coco/', views.coco, name='coco'),
    path('cars3/', views.cars3, name='cars3'),
    path('dory/', views.dory, name='dory'),
    path('dino/', views.dino, name='dino'),
    path('io/', views.io, name='io'),
    path('mu/', views.mu, name='mu'),
    path('brave/', views.brave, name='brave'),
    path('cars2/', views.cars2, name='cars2'),
    path('toy3/', views.toy3, name='toy3'),
    path('up/', views.up, name='up'),
    path('walle/', views.walle, name='walle'),
    path('rat/', views.rat, name='rat'),
    path('cars/', views.cars, name='cars'),
    path('incredibles/', views.incredibles, name='incredibles'),
    path('nemo/', views.nemo, name='nemo'),
    path('monsters/', views.monsters, name='monsters'),
    path('toy2/', views.toy2, name='toy2'),
    path('bug/', views.bug, name='bug'),
    path('toy1/', views.toy1, name='toy1'),
]