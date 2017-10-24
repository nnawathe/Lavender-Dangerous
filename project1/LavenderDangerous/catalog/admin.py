from django.contrib import admin

# Register your models here.
from .models import Product, Category, User, ShoppingCart, Review, Requests


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id', 'quantity', 'description', 'image')
    fields = ['name', 'price', 'id', 'quantity', 'description', 'image']



admin.site.register(Product, ProductAdmin)


class ShoppingCartAdmin(admin.ModelAdmin):
	list_display = ('user', 'get_product')
	fields = ['user','product']

	def get_product():
		return "\n".join([p.products for p in self.product.all()])

admin.site.register(ShoppingCart, ShoppingCartAdmin)

