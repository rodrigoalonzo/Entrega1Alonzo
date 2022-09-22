from django.urls import path
from AppBlog import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('nosotros/', views.blogger, name="Nosotros"),
    path('servicios/', views.services, name="Servicios"),
    path('infoactual/', views.updatedinformation, name="Información"),
    path('vencimientos', views.taxesexpirationdates, name="Vencimientos"),
]