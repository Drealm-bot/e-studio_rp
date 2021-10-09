from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "estudio/home.html")

def quienessomos(request):

    return render(request, "estudio/quienessomos.html")

def servicio(request):

    return render(request, "estudio/servicio.html")

def contacto(request):

    return render(request, "estudio/contacto.html")