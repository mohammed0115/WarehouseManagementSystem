# from django.contrib import admin

# # Register your models here.
# from django import forms
# from django.contrib import admin, messages
# from django.contrib.auth import get_permission_codename

# import datetime
# from .models import Order, OrderProduct, Ship, ShipDetail
# from finance.models import Receivable, ReceivableDetail
# from inventory.models import Ptran


# """
# //Order detail check
# 1.At least one single
# 2.Item is not repeatable
# 3.Whether the product quantity is greater than 0
# """
# class OrderProductCheckInlineFormset(forms.models.BaseInlineFormSet):
#     def clean(self):
#         count = 0
#         product_list = []
#         for form in self.forms:
#             if form.cleaned_data:
#                 count += 1

#                 quantity = form.cleaned_data.get('quantity')
#                 if quantity <= 0:
#                     raise forms.ValidationError(u'The quantity of goods in the order cannot be 0 or negative.')

#                 product_id = form.cleaned_data.get('product')
#                 if product_id in product_list:
#                     raise forms.ValidationError(u'Items in the order must not be duplicated.')
#                 else:
#                     product_list.append(product_id)

#         if count < 1:
#             raise forms.ValidationError(u'You must enter at least one order detail.')


# class OrderProductInline(admin.TabularInline):
#     formset = OrderProductCheckInlineFormset
#     model = OrderProduct
#     fields = ['product', 'quantity', 'description']
#     raw_id_fields = ['product']
#     extra = 0


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'cat_id', 'pi_no', 'po_no', 'customer', 'is_urgency', 'status',
#                     'etd', 'created', 'create_user']
#     fields = ['cat_id', 'po_no', 'customer', 'is_urgency', 'etd']
#     list_filter = ['is_urgency', 'status']
#     actions = ['make_actived']
#     inlines = [OrderProductInline]
#     view_on_site = False
#     list_per_page = 10
#     list_max_show_all = 100
#     date_hierarchy = 'created'

#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.create_user = request.user

#             """
#             pi_no The format is R201901121
#             R:Start
#             201901:2019 January 2013
#             121:Three code water code
#             """
#             pattern = 'R' + datetime.datetime.now().strftime("%Y%m")
#             orders = Order.objects.filter(pi_no__startswith=pattern)
#             obj.pi_no = pattern + "{0:03d}".format(orders.count() + 1)
#         super().save_model(request, obj, form, change)

#     def make_actived(self, request, queryset):
#         rows = queryset.update(is_active=False)
#         if rows > 0:
#             self.message_user(request, u'Order termination action completed')
#     make_actived.allowed_permissions = ('active',)
#     make_actived.short_description = u'Termination order'

#     def has_active_permission(self, request):
#         opts = self.opts
#         codename = get_permission_codename('active', opts)
#         return request.user.has_perm('%s.%s' % (opts.app_label, codename))


# admin.site.register(Order, OrderAdmin)


# """
# //Delivery order detail check
# 1.At least one single
# 2.Whether the inventory of goods is sufficient
# 3.Whether at least one shipment quantity is greater than 0
# 4.Shipment quantity must not be negative
# 4.Single products shall not be repeated
# """
# class ShipDetailCheckInlineFormset(forms.models.BaseInlineFormSet):
#     def clean(self):
#         detail_count = 0
#         detail_amount = 0

#         product_list = []
#         for form in self.forms:
#             if form.cleaned_data:
#                 detail_count += 1

#                 quantity = form.cleaned_data.get('quantity')
#                 if quantity < 0:
#                     raise forms.ValidationError(u'The quantity of goods in the delivery note shall not be negative.')
#                 elif quantity > 0:
#                     detail_amount += 1

#                 product = form.cleaned_data.get('product')
#                 quantity = int(form.cleaned_data.get('quantity'))
#                 if product.stock < quantity:
#                     raise forms.ValidationError(u"commodity[{}-{}]Stock {}，Unable to meet this shipment {}，"
#                                                 u"Please fill in the process sheet first to increase the inventory.".format(product.id, product.title,
#                                                                          product.stock, quantity))

#                 if product.id in product_list:
#                     raise forms.ValidationError(u"Single commodity[{}-{}]Has been repeated."
#                                                 u"Please fill in the shipping order again.".format(product.id, product.title))
#                 else:
#                     product_list.append(product.id)
#         if detail_count < 1:
#             raise forms.ValidationError(u'You must enter at least one order detail')
#         if detail_amount < 1:
#             raise forms.ValidationError(u'You must have at least one shipment order detail quantity greater than 0')


# class ShipDetailInline(admin.TabularInline):
#     formset = ShipDetailCheckInlineFormset
#     model = ShipDetail
#     fields = ['product', 'quantity', 'description']
#     raw_id_fields = ['product']
#     extra = 0


# """
# //Relevant actions during shipment are as follows:
# 1.For each shipping order detail
#    i.New goods inventory changes(Ptran)
#   ii.If quantity shipped>0 Add detail of accounts receivable(ReceivableDetail)
#  iii.Reduce inventory(product.stock)
# 2.For the entire shipping order
#    i.Change the status of the shipment order to effective shipment(is_active=True) Check whether the delivery date is delayed(is_delay)
#   ii.If quantity shipped>0 A new account receivable will be added(Receivable)
#  iii.Check whether the order quantity is satisfied and determine the order"state"，('A', 'All shipments'),('P', 'Partial shipment')
# """
# class ShipAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'customer', 'is_active', 'is_delay', 'created', 'create_user']
#     fields = ['order']
#     actions = ['make_actived']
#     inlines = [ShipDetailInline]
#     view_on_site = False
#     list_per_page = 10
#     list_max_show_all = 100
#     date_hierarchy = 'created'

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'order':
#             kwargs['queryset'] = Order.objects.filter(is_active=True).exclude(status='A')
#         return super(ShipAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.create_user = request.user
#             order = obj.order
#             obj.customer = order.customer
#         super().save_model(request, obj, form, change)

#     def save_related(self, request, form, formsets, change):
#         super().save_related(request, form, formsets, change)

#         ship = form.save(commit=False)

#         #Add a / R header
#         receivable = Receivable()
#         receivable.ship = ship
#         receivable.customer = ship.customer
#         #A / R date = delivery date + accounting period
#         receivable.receivabled = datetime.datetime.now().date() + datetime.timedelta(days=ship.customer.period.period)
#         receivable.create_user = ship.create_user
#         receivable.save()

#         ship_details = ShipDetail.objects.filter(ship=ship)
#         for ship_detail in ship_details:
#             #New goods inventory changes
#             product = ship_detail.product
#             stock = product.stock
#             tran_quantity = ship_detail.quantity

#             ptran = Ptran()
#             ptran.product = product
#             ptran.source_form = 'SHIP'
#             ptran.source_id = ship.id
#             ptran.from_quantity = stock
#             ptran.tran_quantity = 0 - tran_quantity
#             ptran.to_quantity = stock - tran_quantity
#             ptran.create_user = request.user
#             ptran.save()

#             #New account receivable detail
#             receivable_detail = ReceivableDetail()
#             receivable_detail.receivable = receivable
#             receivable_detail.product = product
#             receivable_detail.amount = product.tax_price * tran_quantity
#             receivable_detail.currency = product.currency
#             receivable_detail.save()

#             #Reduce inventory
#             product.stock = stock - tran_quantity
#             product.save()

#         order = form.cleaned_data.get('order')
#         #Modify shipment status
#         ship.is_active = True
#         today = datetime.datetime.now().date()
#         if today > order.etd:
#             ship.is_delay = True
#         ship.save()

#         #Determines the status of the corresponding order ('A ',' all shipments'), ('P ',' part shipments'), ('O ',' over shipment '). If there is an order detail quantity that is not all shipped out, the status is P
#         order_products = OrderProduct.objects.filter(order=order)
#         ships = Ship.objects.filter(order=order)
#         status = 'A'
#         for order_product in order_products:
#             product = order_product.product
#             shipped_quantity = 0
#             for ship in ships.all():
#                 ship_details = ShipDetail.objects.filter(product=product, ship=ship)
#                 if ship_details.all().count() > 0:
#                     for ship_detail in ship_details.all():
#                         shipped_quantity += ship_detail.quantity

#             if shipped_quantity < order_product.quantity:
#                 status = 'P'
#             else:
#                 if shipped_quantity > order_product.quantity:
#                     #If some goods are part of the shipment P, even if there is excess shipment p
#                     if status is 'P':
#                         status = 'P'
#                     else:
#                         status = 'O'

#         order.status = status
#         order.save()

#         #Modify accounts receivable status if no error occurs
#         receivable.is_active = True
#         receivable.save()

#     def make_actived(self, request, queryset):
#         rows = queryset.update(is_active=False)
#         if rows > 0:
#             self.message_user(request, u'Finished terminating the shipping order')
#     make_actived.allowed_permissions = ('active',)
#     make_actived.short_description = u'Terminate shipping order'

#     def has_active_permission(self, request):
#         opts = self.opts
#         codename = get_permission_codename('active', opts)
#         return request.user.has_perm('%s.%s' % (opts.app_label, codename))


# admin.site.register(Ship, ShipAdmin)