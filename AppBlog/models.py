from django.db import models

#Modelos creados

class Blogger(models.Model):

    bloggername = models.CharField(max_length=100)
    bloggersurname = models.CharField(max_length=100)
    bloggerprofesion = models.CharField(max_length=100)
    bloggeremail = models.EmailField()
    bloggercellnumber = models.IntegerField()

class Services(models.Model):

    servicename = models.CharField(max_length=100)

class Updatedinformation(models.Model):

    bloggername = models.CharField(max_length=100)
    informationdate = models.DateField()
    informationtext = models.CharField(max_length=500)

class Taxexpirationdates(models.Model):

    taxname = models.CharField(max_length=100)
    taxdate = models.DateField()
    taxresponsible = models.CharField(max_length=100)
