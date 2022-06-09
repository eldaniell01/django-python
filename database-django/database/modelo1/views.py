from ast import arg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Aeropuerto, Vuelos, Pasajero
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "vuelos/index.html",{
        "vuelos": Vuelos.objects.all()
    })
    
def vuelo(request, vuelo_id):
    vuelo= Vuelos.objects.get(pk=vuelo_id)
    return render(request, "vuelos/vuelo.html",{
        "vuelo": vuelo,
        "pasajero": vuelo.pasajero.all(),
        "no_pasajero": Pasajero.objects.exclude(vuelos=vuelo).all()
    })

def book(request, vuelo_id):
    if request.method== 'POST':
        vue = Vuelos.objects.get(pk=vuelo_id)
        print(vue)
        pasajeros = Pasajero.objects.get(pk=int(request.POST["pasajero"]))
        print(pasajeros)
        pasajeros.vuelos.add(vue)
        print(pasajeros)
        return HttpResponseRedirect(reverse("vuelo", args=(vue.id,)))