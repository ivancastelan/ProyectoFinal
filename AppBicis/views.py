from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *


# Create your views here.

def home(request):
    return render(request, "AppBicis/inicio.html")



def BiciVender(request):

    if request.method=="POST":

        biciVender = FormularioBiciVend(request.POST)
        if biciVender.is_valid():

            info = biciVender.cleaned_data

            biciF = VenderBici(bici=info["bici"],
            tipo = info["tipo"],
            precio = info["precio"],
            vendEmail = info["vendEmail"],
            vendTel = info["vendTel"])
            biciF.save()

            return render(request, "AppBicis/inicio.html")
        
    else:
        biciVender: FormularioBiciVend()
        
    return render(request, "AppBicis/biciVender.html")



def CambiarBici(request):

    if request.method=="POST":

        biciCambiar = FormularioBiciCamb(request.POST)   

        if biciCambiar.is_valid():

            info = biciCambiar.cleaned_data

            biciF = BiciCambiar(bici=info["bici"],
            tipo = info["tipo"],
            precio = info["precio"])
            biciF.save()

            return render(request, "AppBicis/inicio.html")
        
    else:
        biciCambiar: FormularioBiciCamb()

    return render(request, "AppBicis/biciCambiar.html")
    



def busquedaBici(request):

    return render(request, "AppBicis/buscarBicis.html")


def resultadoBusqueda(request):

    if request.GET['tipo']:

        tipo = request.GET['tipo']
        bicisTipo = VenderBici.objects.filter(tipo__icontains=tipo)
        return render(request, 'AppBicis/resultado.html', {"bicicletas": bicisTipo, "tipo":tipo})

    else:
        respuesta = "No ingresaste datos. Intenta de nuevo."

    return HttpResponse(respuesta)




def leerBicis(request):

    bicis = VenderBici.objects.all()

    contexto = {"biclas": bicis}

    return render(request, "AppBicis/leerBicis.html", contexto)



def crearBici(request):

    if request.method=="POST":

        datosVend = FormularioDatosV(request.POST)
        if datosVend.is_valid():

            info = datosVend.cleaned_data

            vend = DatosVend(nombre=info["nombre"],
            edad = info["edad"],
            direccion = info["direccion"],
            correo = info["correo"],
            telefono = info["telefono"])
            vend.save()

            return render(request, "AppBicis/inicio.html")
        
    else:
        datosVend: FormularioDatosV()

    contexto = {"formVend":datosVend}    
    return render(request, "AppBicis/datosVend.html", contexto)

def eliminarBici(request, biciNombre):

    bicicleta = VenderBici.objects.get(bici=biciNombre)
    bicicleta.delete()

    bicis = VenderBici.objects.all()

    contexto = {"biclas":bicis}

    return render(request, "AppBicis/leerBicis.html", contexto)


def editarDatos(request, biciNombre):

    bicicleta = VenderBici.objects.get(bici=biciNombre)

    if request.method=="POST":

            datosBici = VenderBici(request.POST)
            if datosBici.is_valid():

                info = datosBici.cleaned_data

                bicicleta.bici = info["bici"]
                bicicleta.tipo = info["tipo"]
                bicicleta.precio = info["precio"]
                bicicleta.vendEmail = info["vendEmail"]
                bicicleta.vendTel = info["vendTel"]    

                bicicleta.save()

            return render(request, "AppBicis/inicio.html")
            
    else:
            biciDatos: FormularioBiciVend(initial={"nombre":bicicleta.bici, "tipo":bicicleta.tipo, "precio":bicicleta.precio, 
            "email":bicicleta.vendEmail, "telefono":bicicleta.vendTel})

    contexto = {"DatosBici":biciDatos, "bicis":biciNombre}    
    return render(request, "AppBicis/editarBicis.html", contexto)
