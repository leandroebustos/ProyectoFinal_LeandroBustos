from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "sociedad/index.html")

def pilotos(request):
    contexto = {"pilotos": Piloto.objects.all()}
    return render(request, "sociedad/pilotos.html", contexto)

def autos(request):
    contexto = {"autos": Auto_modelo.objects.all()}
    return render(request, "sociedad/autos.html", contexto)

def resultado(request):
    contexto = {"resultado": Resultado.objects.all()}
    return render(request, "sociedad/tiempos.html", contexto)

def estadisticas(request):
    contexto = {"estadistica": Estadisticas.objects.all()}
    return render(request, "sociedad/posiciones.html",contexto)
