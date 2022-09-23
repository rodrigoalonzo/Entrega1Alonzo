from tkinter import N
from django import forms

#Formularios creados

class ProfessionalsForm(forms.Form):

    Nombre = forms.CharField(max_length=100)
    Apellido = forms.CharField(max_length=100)
    Profesión = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Celular = forms.IntegerField()

class ServicesForm(forms.Form):

    Servicio = forms.CharField(max_length=100)

class UpdatedinformationForm(forms.Form):

    Profesional = forms.CharField(max_length=100)
    Fecha = forms.DateField()
    Texto = forms.CharField(max_length=500)

class TaxexpirationdatesForm(forms.Form):

    Impuesto = forms.CharField(max_length=100)
    Vencimiento = forms.DateField()
    Responsable = forms.CharField(max_length=100)