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
    description=Product.objects.filter(name='Scott 1000 Toilet Paper').first()
    price=Product.objects.filter(name='Scott 1000 Toilet Paper').first().display_price()
    reviewer=Review.objects.first().display_user()
    review_text=Review.objects.first().__str__
    score=Review.objects.first().display_rating()
    reviewer2=Review.objects.first().display_user()
    review2_text=Review.objects.first().__str__
    score2=Review.objects.first().display_rating()

    return render(
        product,
        'product.html',
        context={'description': description, 'price': price, 'reviewer': reviewer, 'review_text': review_text, 
        'score': score, 'reviewer2': reviewer, 'review2_text': review_text, 'score2': score}
        )

def cart(cart):
    item1=ShoppingCart.objects.first().product.first()
    item2=ShoppingCart.objects.first().product.all()[1]
    price1=ShoppingCart.objects.first().product.first().display_price()
    price2=ShoppingCart.objects.first().product.all()[1].display_price()

    return render(
        cart,
        'cart.html',
        context={'item1': item1, 'item2': item2, 'price1': price1, 'price2': price2}
    )

def user(user):
    return render(
        user,
    	'user.html'
    )

def requests(request):
    num_requests=Request.objects.count()
    item1=Request.objects.filter(popularity__gte=1).first()
    user1=Request.objects.filter(popularity__gte=1).first().display_user
    item2=Request.objects.filter(popularity=0).first()
    user2=Request.objects.filter(popularity=0).first().display_user

    return render(
    	request,
    	'requests.html',
    	context={'num_requests':num_requests, 'item1': item1, 'user1': user1,
                    'item2': item2, 'user2': user2}
    )


def faq(faq):
     return render(
        faq,
        'faq.html'
    )
