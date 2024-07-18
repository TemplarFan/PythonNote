from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):    
    return HttpResponse("<h1>Hello NEU. 100Ann.</h1>")
