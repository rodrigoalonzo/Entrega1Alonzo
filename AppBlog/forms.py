from tkinter import N
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    Servicio = forms.CharField(max_length=100)
    Fecha = forms.DateField()
    Titulo = forms.CharField(max_length=100)
    Texto = forms.CharField(max_length=1500)

class TaxexpirationdatesForm(forms.Form):

    Impuesto = forms.CharField(max_length=100)
    Vencimiento = forms.DateField()
    Responsable = forms.CharField(max_length=100)

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme nueva contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]