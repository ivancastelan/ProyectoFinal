from django.db import models

# Create your models here.

class VenderBici(models.Model):

    def __str__(self):
        return f"Bicicleta {self.bici}"

    bici = models.CharField(max_length=40)
    tipo = models.CharField(max_length=25)
    precio = models.IntegerField()
    vendEmail = models.EmailField()
    vendTel = models.IntegerField()


class DatosVend(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models. IntegerField()
    direccion = models.CharField(max_length=80)
    correo = models.EmailField()
    telefono = models.IntegerField()


class BiciCambiar(models.Model):

    def __str__(self):
        return f"Bicicleta {self.bici}"

    bici = models.CharField(max_length=40)
    tipo = models.CharField(max_length=25)
    precio = models.IntegerField()
    



    
