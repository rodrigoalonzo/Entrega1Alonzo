from django.urls import path
from AppBlog import views
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('acercademi/', views.acerca1, name="Acerca"),
    path('acercademi/', views.acerca2, name="Acerca"),
    path('nosotros/', views.professionals, name="Nosotros"),
    path('servicios/', views.services, name="Servicios"),
    path('infoactual/', views.updatedinformation, name="Información"),
    path('vencimientos', views.taxesexpirationdates, name="Vencimientos"),
    path('formprof/', views.FormProfessionals, name="FormProfessionals"),
    path('formserv/', views.FormServices, name="FormServices"),
    path('forminfo/', views.FormUpdateInfo, name="FormUpdatedInfo"),
    path('formtaxes', views.FormTaxesExpiration, name="FormTaxesExpiration"),
    path('searchprofessional/', views.SearchProfessional, name="BuscarProfesional"),
    path('searchprof/', views.ProfSearch),
    path('deleteprof/<profname>', views.ProfDelete, name="DeleteProfessional"),
    path('deleteserv/<servname>', views.ServiceDelete, name="DeleteService"),
    path('deleteinfo/<infotitle>', views.InformationDelete, name="DeleteInformation"),
    path('deletetaxexp/<taxexpname>', views.TaxesExpirationDelete, name="DeleteExpiration"),
    path('profedit/<profname>', views.ProfEdit, name="EditProfessional"),
    path('servedit/<servname>', views.ServiceEdit, name="EditService"),
    path('infoedit/<infoname>', views.InfoEdit, name="EditInformation"),
    path('taxexpedit/<taxexpname>', views.TaxesExpirationEdit, name="EditTaxesExpiration"),
    path('nosotros/profdetails/<int:pk>', DetailsProfessionals.as_view(), name="DetailsProfessionals"),
    path('nosotros/deleteprofq/<int:pk>', ProfessionalConfirmation.as_view(), name="ProfessionalConfirmation"),
    path('servicios/deleteservq/<int:pk>', ServiceConfirmation.as_view(), name="ServiceConfirmation"),
    path('infoactual/deleteinfoq/<int:pk>', InformationConfirmation.as_view(), name="InformationConfirmation"),
    path('vencimientos/deletetaxexpq/<int:pk>', ExpirationConfirmation.as_view(), name="ExpirationConfirmation"),
    path('login/', Login, name="Login"),
    path('register/', Register, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="AppBlog/18logout.html"), name="Logout"),
    path('useredit/', UserEdit, name="EditarUsuario"),
    path('infoactual/infodetails/<int:pk>', DetailsInformation.as_view(), name="DetailsInformation"),
]