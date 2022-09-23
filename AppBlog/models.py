from django.db import models

#Modelos creados

class Professionals(models.Model):

    professionalname = models.CharField(max_length=100)
    professionalsurname = models.CharField(max_length=100)
    professionalprofesion = models.CharField(max_length=100)
    professionalemail = models.EmailField()
    professionalcellnumber = models.IntegerField()

class Services(models.Model):

    servicename = models.CharField(max_length=100)

class Updatedinformation(models.Model):

    professionalname = models.CharField(max_length=100)
    informationdate = models.DateField()
    informationtext = models.CharField(max_length=500)

class Taxexpirationdates(models.Model):

    taxname = models.CharField(max_length=100)
    taxdate = models.DateField()
    taxresponsible = models.CharField(max_length=100)
