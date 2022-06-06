from django.shortcuts import render
from .models import Aeropuerto, Vuelos
# Create your views here.
def index(request):
    return render(request, "vuelos/index.html",{
        "vuelos": Vuelos.objects.all()
    })
    
def vuelo(request, vuelo_id):
    vuelo= Vuelos.objects.get(pk=vuelo_id)
    return render(request, "vuelos/vuelo.html",{
        "vuelo": vuelo,
        "pasajero": vuelo.pasajero.all()
    })