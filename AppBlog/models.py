from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

#Modelos creados

class Professionals(models.Model):

    def __str__(self):
        return f"Profesional: {self.professionalname} {self.professionalsurname} - {self.professionalprofesion}"

    professionalname = models.CharField(max_length=100)
    professionalsurname = models.CharField(max_length=100)
    professionalprofesion = models.CharField(max_length=100)
    professionalemail = models.EmailField()
    professionalcellnumber = models.IntegerField()

class Services(models.Model):

    def __str__(self):
        return f"Servicio: {self.servicename}"

    servicename = models.CharField(max_length=100)

class Updatedinformation(models.Model):

    def __str__(self):
        return f"Actualización: {self.informationdate}"

    professionalname = models.CharField(max_length=100)
    informationservice = models.CharField(max_length=100)
    informationdate = models.DateField()
    informationtitle = models.CharField(max_length=100)
    informationtext = models.CharField(max_length=1500)

class Taxexpirationdates(models.Model):

    def __str__(self):
        return f"Impuesto: {self.taxname} - Vencimiento: {self.taxdate}"

    taxname = models.CharField(max_length=100)
    taxdate = models.DateField()
    taxresponsible = models.CharField(max_length=100)

class UserAvatar(models.Model):

    def __str__(self):
        return f"Avatar de usuario: {self.user}"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="usersavatars", null=True, blank=True)

class AboutMeImage(models.Model):

    imageabout = models.ImageField(upload_to="aboutmeimage", null=True, blank=True)