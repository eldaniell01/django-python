from django import views
from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("daniel",views.daniel, name="daniel"),
    path("alvaro", views.alvaro, name="alvaro")
]