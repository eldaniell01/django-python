from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index/index.html")

def daniel(request):
    return HttpResponse('hola yo')

def alvaro(request):
    return HttpResponse('hello, alvaro')

def greet(request, name):
    return render(request, "index/greet.html", {
        "name": name.capitalize()
    })
