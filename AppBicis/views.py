from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *


# Create your views here.

def home(request):
    return render(request, "AppBicis/inicio.html")

"""""""""""""""""
def BiciVender(request, ):

    bicicleta = BiciVender.objects.get(bici=)
"""""""""""""""