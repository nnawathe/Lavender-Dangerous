from django.shortcuts import render

# Create your views here.

from .models import Product, User, ShoppingCart, Request, Review, Category

def index(request):
    pass
    
class ProductListView(generic.ListView):
    pass
    
def account(request):
    pass
    
def requests(request):
    pass
    
def faq(request):
    pass