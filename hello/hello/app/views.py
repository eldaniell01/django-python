from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("helllo,sdfsd ")

def daniel(request):
    return HttpResponse('hola yo')

def alvaro(request):
    return HttpResponse('hello, alvaro')

def greet(request, name):
    return HttpResponse(f"hello {name.capitalize()}")
