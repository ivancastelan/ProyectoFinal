from django import forms


class FormularioBiciVend(forms.Form):

    bici = forms.CharField()
    tipo = forms.CharField()
    precio = forms.IntegerField()
    vendEmail = forms.EmailField()
    vendTel = forms.IntegerField()


class FormularioDatosV(forms.Form):

    nombre = forms.CharField()
    edad = forms. IntegerField()
    direccion = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.IntegerField()

class FormularioBiciCamb(forms.Form):

    bici = forms.CharField()
    tipo = forms.CharField()
    precio = forms.IntegerField()



