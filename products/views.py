from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    # return HttpResponse('Hello Aradhana')
    return render(request, 'index.html',
                  {'products': products})


def newmethod(request):
    return HttpResponse(" This is new product method in existing product module!")
