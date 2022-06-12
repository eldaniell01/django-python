from django.contrib import admin
from .models import Aeropuerto, Vuelos, Pasajero
# Register your models here.

class Vueloadmin(admin.ModelAdmin):
    list_display = ("id", "origin","destination", "duration")

class Pasajeroadmin(admin.ModelAdmin):
    filter_horizontal = ("vuelos",)

admin.site.register(Aeropuerto)
admin.site.register(Vuelos, Vueloadmin)
admin.site.register(Pasajero, Pasajeroadmin)
