from django.urls import path
from AppBlog import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
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
]