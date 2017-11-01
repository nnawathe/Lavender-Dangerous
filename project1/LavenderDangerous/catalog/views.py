from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.

from .models import Product, User, ShoppingCart, Request, Review, Category

def index(index):
    return render(
        index,
    	'index.html'
    )
    
# class ProductListView(generic.ListView):
#     pass

class ProductListView(ListView):
    model = Product
    def get_context_data(self):
        pass
    
def product(product):
    pass

def cart(cart):
    pass
    
def account(account):
    pass
    
def requests(request):
    num_requests=Request.objects.count()
    return render(
    	request,
    	'requests.html',
    	context={'num_requests':num_requests}
    )

    
def faq(faq):
    pass