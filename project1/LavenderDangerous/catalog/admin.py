from django.contrib import admin

# Register your models here.
from .models import Product, Category, Profile, ShoppingCart, Review, Request


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'description', 'display_category', 'image')
    fields = ['name', 'price', 'quantity', 'description', 'category', 'image']



admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    display = ('name')

admin.site.register(Category, CategoryAdmin)


class ShoppingCartAdmin(admin.ModelAdmin):
	list_display = ('display_user','display_product','quantity')
	fields = ['user','product','quantity']

admin.site.register(ShoppingCart, ShoppingCartAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('display_user','product','rating','review_text')
    fields = ['user','product','rating','review_text']

admin.site.register(Review, ReviewAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('display_user','request_title','request_text','popularity')
    fields = ['user','request_title','request_text','popularity']

admin.site.register(Request, RequestAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','shipping_address','billing_address','account_standing')
    fields = ['user','shipping_address','billing_address','account_standing']

admin.site.register(Profile, ProfileAdmin)
