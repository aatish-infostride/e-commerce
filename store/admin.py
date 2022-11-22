from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import Category, Products, Order

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
