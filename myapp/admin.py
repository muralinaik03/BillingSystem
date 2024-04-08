from django.contrib import admin
from .models import Product, Customer, Employee, Bill,BillItem,ProductItem

# Register your models here.
admin.site.register({Product, Customer, Employee, Bill,BillItem,ProductItem})