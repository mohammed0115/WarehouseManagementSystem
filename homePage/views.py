from django.shortcuts import render

from django.template import Context, loader

from Products.models import Product
# Create your views here.
def index (request):
     return render(request,'Pages/index.html',{})
def customerIndex(request):
     return render(request,'customer/index.html',{})
def vendorIndex(request):
     return render(request,'vendor/index.html',{})
def ProductIndex(request):
     return render(request,'product/index.html',{})