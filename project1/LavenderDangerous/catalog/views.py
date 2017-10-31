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
    num_requests=Request.objects.count()
    return render{
    	request,
    	'requests.html',
    	context={'num_requests', num_requests}
    }

    
def faq(request):
    pass