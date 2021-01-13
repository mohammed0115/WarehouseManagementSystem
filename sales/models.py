from django.db import models
from Products.models import Product
from Customers.models import Customer
# Create your models here.
class orderItem(models.Model):
    product =models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    unit_price = models.FloatField()
    Quantity =models.IntegerField()
class order(models.Model):
    oder_date=models.DateField("date_created", auto_now=True, auto_now_add=False)
    Customer = models.ForeignKey("Customers.Customer", on_delete=models.CASCADE)
    orderItem =models.ForeignKey("sales.orderItem", on_delete=models.CASCADE)
    amount     = models.DecimalField("amount", max_digits=5, decimal_places=2,null=True,blank=True)
    def save(self, *args, **kwargs):
        self.amount=self.orderItem.unit_price*self.orderItem.Quantity
        super(order, self).save(*args, **kwargs)

    

    
