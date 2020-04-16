from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def newmodule (request):
    return HttpResponse('Hello Aradhana'
                        '1 this is your new module!')