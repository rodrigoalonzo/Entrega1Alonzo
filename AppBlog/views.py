from django.shortcuts import render
from django.http import HttpResponse

from AppBlog.forms import ProfessionalsForm, ServicesForm, TaxexpirationdatesForm, UpdatedinformationForm
from AppBlog.models import Professionals, Services, Taxexpirationdates, Updatedinformation

#Vistas creadas

def inicio(request):

    return render(request, "AppBlog/1inicio.html")

def professionals(request):

    return render(request, "AppBlog/2profesionales.html")

def services(request):

    return render(request, "AppBlog/3servicios.html")

def updatedinformation(request):

    return render(request, "AppBlog/4informaciones.html")

def taxesexpirationdates(request):

    return render(request, "AppBlog/5vencimientos.html")

def FormProfessionals(request):

    if request.method=="POST":

        formularioProfesionales = ProfessionalsForm(request.POST)

        if formularioProfesionales.is_valid():

            info = formularioProfesionales.cleaned_data
        
            ProfForm = Professionals(professionalname=info["name"], professionalsurname=info["surname"], professionalprofesion=info["profesion"], professionalemail=info["Email"], professionalcellnumber=info["Número de celular"])
        
            ProfForm.save()

            return render(request, "AppBlog/6FormProf.html")

    else:

        formularioProfesionales=ProfessionalsForm()

    return render(request, "AppBlog/6FormProf.html", {"formularioProfesionales":formularioProfesionales})

def FormServices(request):

    if request.method=="POST":

        formularioServicios = ServicesForm(request.POST)

        if formularioServicios.is_valid():

            info = formularioServicios.cleaned_data
        
            ServForm = Services(servicename=info["name"])
        
            ServForm.save()

            return render(request, "AppBlog/7FormServ.html")

    else:

        formularioServicios=ServicesForm()

    return render(request, "AppBlog/7FormServ.html", {"formularioServicios":formularioServicios})

def FormUpdateInfo(request):

    if request.method=="POST":

        formularioInformacion = UpdatedinformationForm(request.POST)

        if formularioInformacion.is_valid():

            info = formularioInformacion.cleaned_data
        
            InfoForm = Updatedinformation(professionalname=info["name"], informationdate=info["date"], informationtext=info["text"])
        
            InfoForm.save()

            return render(request, "AppBlog/8FormInfo.html")

    else:

        formularioInformacion=UpdatedinformationForm()

    return render(request, "AppBlog/8FormInfo.html", {"formularioInformacion":formularioInformacion})

def FormTaxesExpiration(request):

    if request.method=="POST":

        formularioImpuestos = TaxexpirationdatesForm(request.POST)

        if formularioImpuestos.is_valid():

            info = formularioImpuestos.cleaned_data
        
            ImpForm = Taxexpirationdates(taxname=info["taxname"], taxdate=info["taxdate"], taxresponsible=info["taxresponsible"])
        
            ImpForm.save()

            return render(request, "AppBlog/9FormTaxes.html")

    else:

        formularioImpuestos=TaxexpirationdatesForm()

    return render(request, "AppBlog/9FormTaxes.html", {"formularioImpuestos":formularioImpuestos})