import http
from django.shortcuts import render
from django.http import HttpResponse

#Vistas creadas

def inicio(request):

    return render(request, "AppBlog/1inicio.html")

def blogger(request):

    return render(request, "AppBlog/2profesionales.html")

def services(request):

    return render(request, "AppBlog/3servicios.html")

def updatedinformation(request):

    return render(request, "AppBlog/4informaciones.html")

def taxesexpirationdates(request):

    return render(request, "AppBlog/5vencimientos.html")