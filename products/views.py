from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Hello Aradhana')


def newmethod(request):
    return HttpResponse(" This is new product method in existing product module!")
