from django.urls import path
from sales.views import ItemsCreate

urlpatterns = [
    path('sales/', ItemsCreate.as_views(), name='sale-index'),



]