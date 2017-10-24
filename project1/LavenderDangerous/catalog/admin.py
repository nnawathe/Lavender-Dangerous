from django.contrib import admin

# Register your models here.
from .models import Product, Category, User, ShoppingCart, Review, Requests


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id', 'quantity', 'description', 'image')
    fields = ['name', 'price', 'id', 'quantity', 'description', 'image']



admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ()
