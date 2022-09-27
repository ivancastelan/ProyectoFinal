from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('biciVender/', BiciVender, name="VenderBici"),
    path('biciCambiar/', CambiarBici, name="cambiarBici"),
    path('buscar/', busquedaBici, name="BuscarBici"),
    path('resultado/', resultadoBusqueda, name="resultado"),


]