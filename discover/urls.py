from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.all_films, name='films'),
    path('shorts/', views.all_shorts, name='shorts'),
    path('luca/', views.film_templates, name='luca'),
    path('bao/', views.short_templates, name='bao'),
]