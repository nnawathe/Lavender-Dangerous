from django.shortcuts import render

# Create your views here.

from .models import Product, User, ShoppingCart, Request, Review, Category

def index(index):
    return render(
        index,
    	'index.html'
    )
    
# class ProductListView(generic.ListView):
#     pass

def ProductListView(request):
    pass
    
def product(request):
    pass

def cart(request):
    pass
    
def account(request):
    pass
    
def requests(request):
    num_requests=Request.objects.count()
    return render(
    	request,
    	'requests.html',
    	context={'num_requests':num_requests}
    )

    
def faq(request):
    pass