from django.contrib import admin
from store.models import *

# Register your models here.
admin.site.register([Customer, Product, Order, OrderItem, ShippingAddress])