from django.urls import path
from sales.views import ItemsCreate

urlpatterns = [
    path('sales/', ItemsCreate.as_view(), name='sale-index'),
]