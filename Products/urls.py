from django.urls import path
from Products.views import (ProductDetailView,ProductDelete,
ProductListView,ProductUpdate,ProductCreate,ProductUpdate)

urlpatterns = [
    #...
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/delete/<int:pk>', ProductDelete.as_view(), name='product-delete'),
    path('product/create/', ProductCreate.as_view(), name='product-create'),
    path('product/update/<int:pk>', ProductUpdate.as_view(), name='product-update'),



]