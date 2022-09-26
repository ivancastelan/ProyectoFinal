from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *


# Create your views here.

def home(request):
    return render(request, "AppBicis/inicio.html")


def BiciVender(request):

    if request.method=="POST":

        biciV = BiciVender(bici=request.POST["bici"],
        tipo=request.POST["tipo"],
        precio=request.POST["precio"],
        vendEmail=request.POST["vendEmail"],
        vendTel=request.POST["vendTel"],)

        return render(request, "AppBicis/inicio.html")
        
    return render(request, "AppBicis/biciVender.html")

"""""""""""""""
def BiciVender(request):

    if request.method=="POST":

        biciVender = FormularioBiciVend(request.POST)
        if biciVender.is_valid():

            info = FormularioBiciVend.cleaned_data

            biciF = BiciVender(bici=info["bici"])
            tipo = info["tipo"]
            precio = info["precio"]
            vendEmail = info["vendEmail"]
            vendTel = info["vendTel"]

            biciF.save()
            return render(request, "AppBicis/inicio.html")
        
    else:
        biciVender: FormularioBiciVend()
        
    return render(request, "AppBicis/biciVender.html")
"""""""""
    