# from django.db import models

# # Create your models here.
# CAT_CHOICES = [
#     ('1', 'CAT1'),
#     ('2', 'CAT2'),
#     ('3', 'CAT3'),
# ]


# ORDER_CHOICES = [
#     ('N', u'Not yet shipped'),
#     ('A', u'All shipments'),
#     ('P', u'Partial shipment'),
#     ('O', u'Excess shipment'),
# ]


# class Order(models.Model):
#     cat_id = models.CharField(max_length=2, choices=CAT_CHOICES, blank=False, verbose_name=u'Cat.')
#     pi_no = models.CharField(max_length=16, verbose_name='PI #', blank=False, null=False, unique=True)
#     po_no = models.CharField(max_length=16, verbose_name='PO #', blank=True)
#     customer = models.ForeignKey(Customer, verbose_name=u'Customer', on_delete=models.PROTECT,
#                                  limit_choices_to={'status': 'A'},)
#     is_active = models.BooleanField(verbose_name=u'Is it effective?', default=True)
#     is_urgency = models.BooleanField(verbose_name=u'Urgent order or not', default=False)
#     status = models.CharField(max_length=1, choices=ORDER_CHOICES, default='N', verbose_name=u'state')
#     etd = models.DateField(blank=False, null=False, verbose_name=u'Scheduled delivery date')
#     created = models.DateTimeField(auto_now_add=True, verbose_name=u'Order time')
#     create_user = models.ForeignKey('auth.User', verbose_name=u'Staff establishment', on_delete=models.PROTECT)

#     def get_absolute_url(self):
#         return reverse('sale:order_detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return 'Id:{}-PI #:{}- PO #:{}'.format(self.id, self.pi_no, self.po_no)

#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = verbose_name
#         permissions = (
#             ('active_order', 'Order can be suspended'),
#         )














# class OrderProduct(models.Model):
#     num = models.CharField(max_length=2, default='', verbose_name=u'Single item')
#     order = models.ForeignKey(Order, verbose_name=u'Order sheet', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, verbose_name=u'commodity', on_delete=models.DO_NOTHING,
#                                 limit_choices_to={'status': 'A'},)
#     quantity = models.PositiveIntegerField(blank=False, verbose_name=u'Order quantity')
#     price = models.DecimalField(max_digits=16, decimal_places=4, blank=False, verbose_name=u'Non tax amount')
#     tax = models.DecimalField(max_digits=16, decimal_places=4, blank=False, verbose_name=u'Taxes')
#     tax_price = models.DecimalField(max_digits=16, decimal_places=4, blank=False, verbose_name=u'Tax amount')
#     subtotal = models.DecimalField(max_digits=16, decimal_places=4, blank=False, verbose_name=u'Subtotal amount not taxed')
#     tax_subtotal = models.DecimalField(max_digits=16, decimal_places=4, blank=False, verbose_name=u'Subtotal amount including tax')
#     currency = models.ForeignKey(Currency, verbose_name=u'currency', blank=False, on_delete=models.DO_NOTHING)
#     description = models.CharField(max_length=256, verbose_name=u'describe', blank=True)

#     def save(self, *args, **kwargs):
#         if self.num == '':
#             #The format of the item is 01,02
#             order_products = OrderProduct.objects.filter(order=self.order)
#             num = "{0:02d}".format(order_products.count() + 1)
#             self.num = "{0:02d}".format(int(num))

#         product = Product.objects.get(title=self.product)
#         self.price = product.price
#         self.tax = product.tax
#         self.currency = product.currency
#         self.tax_price = product.tax_price
#         self.subtotal = product.price * self.quantity
#         self.tax_subtotal = product.tax_price * self.quantity
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return '{}'.format(self.num)

#     class Meta:
#         verbose_name = 'Order single'
#         verbose_name_plural = verbose_name




# class Ship(models.Model):
#     order = models.ForeignKey(Order, verbose_name=u'Corresponding orders', on_delete=models.PROTECT)
#     customer = models.ForeignKey(Customer, verbose_name=u'Customer', on_delete=models.PROTECT,
#                                  limit_choices_to={'status': 'A'})
#     is_active = models.BooleanField(verbose_name=u'Is it effective?', default=False)
#     is_delay = models.BooleanField(verbose_name=u'Is it delayed?', default=False)
#     created = models.DateTimeField(auto_now_add=True, verbose_name=u'Shipping time')
#     create_user = models.ForeignKey('auth.User', verbose_name=u'Staff establishment', on_delete=models.PROTECT)

#     def get_absolute_url(self):
#         return reverse('sale:ship_detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return '{}'.format(self.id)

#     class Meta:
#         verbose_name = 'Bill of sales'
#         verbose_name_plural = verbose_name
#         permissions = (
#             ('active_ship', 'Can suspend shipping order'),
#         )
# class ShipDetail(models.Model):
#     num = models.CharField(max_length=2, default='', verbose_name=u'Single item')
#     ship = models.ForeignKey(Ship, verbose_name=u'Shipping order header', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, verbose_name=u'Goods shipped', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(blank=False, verbose_name=u'Quantity shipped')
#     description = models.CharField(max_length=256, verbose_name=u'describe', blank=True)

#     def save(self, *args, **kwargs):
#         if self.num == '':
#             #The format of the item is 01,02
#             ship_detail = ShipDetail.objects.filter(ship=self.ship)
#             num = "{0:02d}".format(ship_detail.count() + 1)
#             self.num = "{0:02d}".format(int(num))
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return '{}'.format(self.num)

#     class Meta:
#         verbose_name = 'Shipping order detail'
#         verbose_name_plural = verbose_name