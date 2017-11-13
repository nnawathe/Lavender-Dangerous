from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Product, User, ShoppingCart, Request, Review, Category

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
    item1=ShoppingCart.objects.first().product.first()
    item2=ShoppingCart.objects.first().product.all()[1]
    price1=ShoppingCart.objects.first().product.first().display_price()
    price2=ShoppingCart.objects.first().product.all()[1].display_price()
    subtotal=price1+price2
    shipping=3.99
    total=shipping+subtotal

    return render(
        cart,
        'cart.html',
        context={'item1': item1, 'item2': item2, 'price1': price1, 'price2': price2, 'subtotal': subtotal,
        'total': total, 'shipping': shipping}
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
