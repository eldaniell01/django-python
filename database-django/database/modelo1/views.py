from django.shortcuts import render
from .models import Aeropuerto, Vuelos
# Create your views here.
def index(request):
    return render(request, "vuelos/index.html",{
        "vuelos": Vuelos.objects.all()
    })