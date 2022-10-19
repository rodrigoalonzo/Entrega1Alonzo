from datetime import date, datetime, timedelta
from django.utils import timezone
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
import AppBlog
from AppBlog.forms import ProfessionalsForm, ServicesForm, TaxexpirationdatesForm, UpdatedinformationForm, UserEditForm, UserRegisterForm
from AppBlog.models import AboutMeImage, Professionals, Services, Taxexpirationdates, Updatedinformation, UserAvatar
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Vistas creadas

def inicio(request):

    return render(request, "AppBlog/1inicio.html")

def acerca1(request):

    aboutmeimage = AboutMeImage.objects.all()

    return render(request, "AppBlog/100acercademi.html", {"aboutmeimage":aboutmeimage})

def acerca2(request):

    today = date.today()

    birthday = date(year=1989, month=7, day=15)

    myage = int(((today-birthday).days)/365)

    return render(request, "AppBlog/100acercademi.html", {"age":myage})

def professionals(request):

    professionalsall = Professionals.objects.all()

    return render(request, "AppBlog/2profesionales.html", {"professionalsall":professionalsall})

def services(request):

    servicesall = Services.objects.all()

    return render(request, "AppBlog/3servicios.html", {"servicesall":servicesall})

def updatedinformation(request):

    updatedinformationall = Updatedinformation.objects.all()

    return render(request, "AppBlog/4informaciones.html", {"updatedinformationall":updatedinformationall})

def taxesexpirationdates(request):

    taxesexpirationdatesall = Taxexpirationdates.objects.all()

    return render(request, "AppBlog/5vencimientos.html", {"taxesexpirationdatesall":taxesexpirationdatesall})

@login_required
def FormProfessionals(request):

    if request.method=="POST":

        formularioProfesionales = ProfessionalsForm(request.POST)

        if formularioProfesionales.is_valid():

            info = formularioProfesionales.cleaned_data
        
            ProfForm = Professionals(professionalname=request.POST["Nombre"], professionalsurname=request.POST["Apellido"], professionalprofesion=request.POST["Profesión"], professionalemail=request.POST["Email"], professionalcellnumber=request.POST["Celular"])
        
            ProfForm.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioProfesionales=ProfessionalsForm()

    return render(request, "AppBlog/6FormProf.html", {"formularioProfesionales":formularioProfesionales})

@login_required
def FormServices(request):

    if request.method=="POST":

        formularioServicios = ServicesForm(request.POST)

        if formularioServicios.is_valid():

            info = formularioServicios.cleaned_data
        
            ServForm = Services(servicename=info["Servicio"])
        
            ServForm.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioServicios=ServicesForm()

    return render(request, "AppBlog/7FormServ.html", {"formularioServicios":formularioServicios})

@login_required
def FormUpdateInfo(request):

    if request.method=="POST":

        formularioInformacion = UpdatedinformationForm(request.POST)

        if formularioInformacion.is_valid():

            info = formularioInformacion.cleaned_data
        
            InfoForm = Updatedinformation(professionalname=info["Profesional"], informationservice=info["Servicio"], informationdate=info["Fecha"], informationtitle=info["Titulo"], informationtext=info["Texto"])
        
            InfoForm.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioInformacion=UpdatedinformationForm()

    return render(request, "AppBlog/8FormInfo.html", {"formularioInformacion":formularioInformacion})

@login_required
def FormTaxesExpiration(request):

    if request.method=="POST":

        formularioImpuestos = TaxexpirationdatesForm(request.POST)

        if formularioImpuestos.is_valid():

            info = formularioImpuestos.cleaned_data
        
            ImpForm = Taxexpirationdates(taxname=info["Impuesto"], taxdate=info["Vencimiento"], taxresponsible=info["Responsable"])
        
            ImpForm.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioImpuestos=TaxexpirationdatesForm()

    return render(request, "AppBlog/9FormTaxes.html", {"formularioImpuestos":formularioImpuestos})

def SearchProfessional(request):

    return render(request, "AppBlog/10FormProfSearch.html")

def ProfSearch(request):

    if request.GET["professionalprofesion"]:
        
        search = request.GET["professionalprofesion"]
        profesionales = Professionals.objects.filter(professionalprofesion__icontains=search)

        return render(request, "AppBlog/11results.html", {"profesionales":profesionales, "search":search})

    else:

        mensaje = "No enviaste datos"

    return render(request, "AppBlog/11resultsnone.html", {"mensaje":mensaje})

@login_required
def ProfDelete(request, profname):

    profdeletename = Professionals.objects.get(professionalname=profname)

    profdeletename.delete()

    professionalsall = Professionals.objects.all()

    return render(request, "AppBlog/2profesionales.html", {"professionalsall":professionalsall})

@login_required
def ServiceDelete(request, servname):

    servdeletename = Services.objects.get(servicename=servname)

    servdeletename.delete()

    servicesall = Services.objects.all()

    return render(request, "AppBlog/3servicios.html", {"servicesall":servicesall})

@login_required
def InformationDelete(request, infotitle):

    infodeletetitle = Updatedinformation.objects.get(informationtitle=infotitle)

    infodeletetitle.delete()

    updatedinformationall = Updatedinformation.objects.all()

    return render(request, "AppBlog/4informaciones.html", {"updatedinformationall":updatedinformationall})

@login_required
def TaxesExpirationDelete(request, taxexpname):

    taxesdeleteexp = Taxexpirationdates.objects.get(taxname=taxexpname)

    taxesdeleteexp.delete()

    taxesexpirationdatesall = Taxexpirationdates.objects.all()

    return render(request, "AppBlog/5vencimientos.html", {"taxesexpirationdatesall":taxesexpirationdatesall})

@login_required
def ProfEdit(request, profname):

    profeditname = Professionals.objects.get(professionalname=profname)

    if request.method == "POST":

        formularioProfesionales = ProfessionalsForm(request.POST)

        if formularioProfesionales.is_valid():

            info = formularioProfesionales.cleaned_data

            profeditname.professionalname = info["Nombre"]
            profeditname.professionalsurname = info["Apellido"]
            profeditname.professionalprofesion = info["Profesión"]
            profeditname.professionalemail = info["Email"]
            profeditname.professionalcellnumber = info["Celular"]

            profeditname.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioProfesionales=ProfessionalsForm(initial={
            "Nombre":profeditname.professionalname,
            "Apellido":profeditname.professionalsurname,
            "Profesión":profeditname.professionalprofesion,
            "Email":profeditname.professionalemail,
            "Celular":profeditname.professionalcellnumber
        })

    return render(request, "AppBlog/12FormProfEdit.html", {"formularioProfesionales":formularioProfesionales, "profeditname":profeditname})

@login_required
def ServiceEdit(request, servname):

    serveditname = Services.objects.get(servicename=servname)

    if request.method == "POST":

        formularioServicios = ServicesForm(request.POST)

        if formularioServicios.is_valid():

            info = formularioServicios.cleaned_data

            serveditname.servicename = info["Servicio"]

            serveditname.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioServicios=ServicesForm(initial={
            "Servicio":serveditname.servicename,
        })

    return render(request, "AppBlog/22FormServEdit.html", {"formularioServicios":formularioServicios, "serveditname":serveditname})

@login_required
def InfoEdit(request, infoname):

    infoeditname = Updatedinformation.objects.get(informationtitle=infoname)

    if request.method == "POST":

        formularioInformacion = UpdatedinformationForm(request.POST)

        if formularioInformacion.is_valid():

            info = formularioInformacion.cleaned_data

            infoeditname.professionalname = info["Profesional"]
            infoeditname.informationservice = info["Servicio"]
            infoeditname.informationdate = info["Fecha"]
            infoeditname.informationtitle = info["Titulo"]
            infoeditname.informationtext = info["Texto"]

            infoeditname.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioInformacion=UpdatedinformationForm(initial={
            "Profesional":infoeditname.professionalname,
            "Servicio":infoeditname.informationservice,
            "Fecha":infoeditname.informationdate,
            "Titulo":infoeditname.informationtitle,
            "Texto":infoeditname.informationtext,
        })

    return render(request, "AppBlog/23FormInfoEdit.html", {"formularioInformacion":formularioInformacion, "infoeditname":infoeditname})

@login_required
def TaxesExpirationEdit(request, taxexpname):

    taxexpeditname = Taxexpirationdates.objects.get(taxname=taxexpname)

    if request.method == "POST":

        formularioVencimientos = TaxexpirationdatesForm(request.POST)

        if formularioVencimientos.is_valid():

            info = formularioVencimientos.cleaned_data

            taxexpeditname.taxname = info["Impuesto"]
            taxexpeditname.taxdate = info["Vencimiento"]
            taxexpeditname.taxresponsible = info["Responsable"]

            taxexpeditname.save()

            return render(request, "AppBlog/1inicio.html")

    else:

        formularioVencimientos=TaxexpirationdatesForm(initial={
            "Impuesto":taxexpeditname.taxname,
            "Vencimiento":taxexpeditname.taxdate,
            "Responsable":taxexpeditname.taxresponsible,
        })

    return render(request, "AppBlog/24FormTaxExpEdit.html", {"formularioVencimientos":formularioVencimientos, "taxexpeditname":taxexpeditname})

class DetailsProfessionals(DetailView):
    model = Professionals
    template_name = "AppBlog/13FormProfDetails.html"

class ProfessionalConfirmation(DetailView):
    model = Professionals
    template_name = "AppBlog/25profdelete.html"

class ServiceConfirmation(DetailView):
    model = Services
    template_name = "AppBlog/26servdelete.html"

class InformationConfirmation(DetailView):
    model = Updatedinformation
    template_name = "AppBlog/27infodelete.html"

class ExpirationConfirmation(DetailView):
    model = Taxexpirationdates
    template_name = "AppBlog/28taxexpdelete.html"

def Login(request):

    if request.method=="POST": #le doy click al boton iniciar sesión
        
        loginform = AuthenticationForm(request, data=request.POST)

        if loginform.is_valid(): #analiza si mi formulario es válido
            
            loginuser = loginform.cleaned_data.get("username")
            loginpassword = loginform.cleaned_data.get("password")

            userlogin = authenticate(username=loginuser, password=loginpassword)

            if userlogin:
                
                login(request, userlogin)

                return render(request, "AppBlog/15loginstate.html", {"loginmessage":f"¡HOLA {userlogin}!"})
            
        else:

            return render(request, "AppBlog/15loginstate.html", {"loginmessage":f"¡DATOS INCORRECTOS!"})

    else:

        loginform = AuthenticationForm()

    return render(request, "AppBlog/14login.html", {"loginform":loginform})

def Register(request):

    if request.method=="POST":

        registerform = UserRegisterForm(request.POST)

        #registerform = UserCreationForm(request.POST)

        if registerform.is_valid():

            newusername = registerform.cleaned_data["username"]
            registerform.save()

            return render(request, "AppBlog/17registerstate.html", {"registermessage":f"¡USUARIO {newusername} CREADO CON ÉXITO!"})

    else:

        registerform = UserRegisterForm()

        #registerform = UserCreationForm()

    return render(request, "AppBlog/16register.html", {"registerform":registerform})

@login_required
def UserEdit(request):

    loggedinuser = request.user

    if request.method=="POST":

        editthisuser = UserEditForm(request.POST)

        if editthisuser.is_valid():

            editinfo = editthisuser.cleaned_data

            loggedinuser.first_name = editinfo["first_name"]
            loggedinuser.last_name = editinfo["last_name"]
            loggedinuser.email = editinfo["email"]
            loggedinuser.password1 = editinfo["password1"]
            loggedinuser.password2 = editinfo["password2"]

            loggedinuser.save()

            return render(request, "AppBlog/20usereditstate.html", {"usereditmessage":f"¡USUARIO {loggedinuser} MODIFICADO CON ÉXITO!"})

    else:

        editthisuser = UserEditForm(initial={
           "first_name":loggedinuser.first_name,
           "last_name":loggedinuser.last_name,
           "email":loggedinuser.email,
        })

    contextuseredit = {"usereditform":editthisuser, "userlogged":loggedinuser}

    return render(request, "AppBlog/19useredit.html", contextuseredit)

class DetailsInformation(DetailView):
    model = Updatedinformation
    template_name = "AppBlog/21infodetails.html"