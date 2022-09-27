from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('biciVender/', BiciVender, name="VenderBici"),
    path('biciCambiar/', CambiarBici, name="cambiarBici"),
    path('buscar/', busquedaBici, name="BuscarBici"),
    path('resultado/', resultadoBusqueda, name="resultado"),
   
   #CRUD - Create, Read, Update and Delete
    path('leerBicis/', leerBicis, name="LeerBiclas"),
    path('crearDatos/', crearBici, name="CrearBiclas"),
    path('borrarBici/<biciNombre>', eliminarBici, name="BorrarBiclas"),
    path('editarBici/<biciNombre>', editarDatos, name="EditarBiclas"),




]