from django.db import models

# Create your models here.
from Products.models import Product
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
class Stores(models.Model):
    name = models.CharField("Inventory Name", max_length=50)
    city   = models.CharField("city", max_length=50)
    email   = models.EmailField("Email", max_length=254)
    phone   = models.CharField("phone number", max_length=50)

    

    class Meta:
        verbose_name = "Stocks"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.name

class Stocks(models.Model):
    name = models.CharField("Inventory Name", max_length=50)
    Product =models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    Stores =models.ForeignKey(Stores, verbose_name="Stores", on_delete=models.CASCADE)
    quan_in_stock = models.IntegerField("Total In")
    sales_quan    = models.IntegerField("Total out")
    real_Quantity = models.IntegerField()

    

    class Meta:
        verbose_name = "Stocks"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Inventory_detail", kwargs={"pk": self.pk})
