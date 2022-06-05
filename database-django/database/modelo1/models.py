from django.db import models

# Create your models here.
class Aeropuerto(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.city}({self.code})"

class Vuelos(models.Model):
    origin = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, related_name="llegada")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"