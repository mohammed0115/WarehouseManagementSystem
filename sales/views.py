from django.shortcuts import render

# Create your views here.
def index (request):
    context={
     "product":"product",
     "Invoice":"invoice"


    }
    return render(request,"Sales/index.html",{})

from django.shortcuts import render
from django.urls import reverse_lazy,reverse
# from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from Products.models import Product
# from Products.forms import ProductForm
from sales.models import *


class ItemsCreate(CreateView):
    models= orderItem
    template_name="sale/index.html"
    # success_url = reverse_lazy('product-list')