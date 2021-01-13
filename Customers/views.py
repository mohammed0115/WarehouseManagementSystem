from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy,reverse
# from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
# from django.views.generic.edit import FormView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from .models import Customer
# from indexs.forms import indexForm


class CustomerCreate(CreateView):
    model = Customer
    fields=['nationalno','fname','minName','lname','email','phone']
    template_name="customer/customer.html"
    success_url = reverse_lazy('customer-list')
class CustomerUpdate(UpdateView):
    model = Customer
    fields=['nationalno','fname','minName','lname','email','phone']
    success_url = reverse_lazy('customer-list')
    template_name="customer/customer.html"
    # def get_context_data(self, **kwargs):
    #     kwargs["object"] = Customer.objects.get(pk=kwargs['pk'])
    #     return super(CustomerUpdate, self).get_context_data(**kwargs)

class CustomerDelete(DeleteView):
    # form_class = indexForm
    model= Customer
    success_url = reverse_lazy('customer:customer-list')
    template_name="customer/customer_confirm_delete.html"
    # def get_success_url(self):
    #     return reverse("cucustomer-list",kwargs={"pk" :self.object.id})

class CustomerDetailView(DetailView):
    model= Customer
    template_name="customer/index.html"

class CustomerListView(ListView):
    queryset= Customer.objects.all()
    template_name="customer/index.html"
