from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request:HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'base.html', context=context)
