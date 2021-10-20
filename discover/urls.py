from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_films, name='films'),
    path('', views.all_shorts, name='shorts'),
]