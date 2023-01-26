from django.shortcuts import render

# Create your views here.

#3.4 Creating a view

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")
