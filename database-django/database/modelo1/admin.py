from django.contrib import admin
from .models import Aeropuerto, Vuelos, Pasajero
# Register your models here.

admin.site.register(Aeropuerto)
admin.site.register(Vuelos)
admin.site.register(Pasajero)
