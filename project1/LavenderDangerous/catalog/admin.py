from django.contrib import admin

# Register your models here.
from .models import Product, Category, User, ShoppingCart, Review, Requests


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id', 'quantity', 'description', 'display_category', 'image')
    fields = ['name', 'price', 'id', 'quantity', 'description', 'category', 'image']



admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    display = ('name')
    
admin.site.register(Category, CategoryAdmin)


class ShoppingCartAdmin(admin.ModelAdmin):
	list_display = ('user', 'get_product')
	fields = ['user','product']

admin.site.register(ShoppingCart, ShoppingCartAdmin)

