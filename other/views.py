from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse("HOLA como estas")
# Create your views here.
