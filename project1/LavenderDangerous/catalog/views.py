from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.contrib.auth.models import User
from .models import Product, Profile, ShoppingCart, Request, Review, Category

def index(index):
    return render(
        index,
    	'index.html'
    )

# class ProductListView(generic.ListView):
#     pass

class ProductListView(generic.ListView):
    model = Product
    
class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['rvw'] = Review.objects.filter(product_id=self.kwargs['pk']).all()
        return context

def cart(cart):
    if cart.user.is_authenticated:
        items=ShoppingCart.objects.filter(user=cart.user).first()
        if items != None:
            items = items.product.all()
            subtotal = 0
            for item in items:
                subtotal += item.price
            shipping=3.99
            total=shipping+subtotal
        else:
            subtotal=0
            shipping=0
            total=0
    else:
        items=None
        subtotal=0
        shipping=0
        total=0

    return render(
        cart,
        'cart.html',
        context={'items': items, 'subtotal': subtotal, 'total': total, 'shipping': shipping}
    )

def user(user):
    return render(
        user,
    	'user.html'
    )

def requests(request):
    num_requests=Request.objects.count()
    rquests=Request.objects.order_by('-popularity').all()

    return render(
    	request,
    	'requests.html',
    	context={'num_requests':num_requests, 'rquests': rquests}
    )


def faq(faq):
     return render(
        faq,
        'faq.html'
    )
