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
    temp = []
    if cart.user.is_authenticated:
        items = ShoppingCart.objects.filter(user=cart.user)
        if items != None:
            subtotal = 0
            for item in items:
                item=item.product
                temp.append(item)
                subtotal += item.price*ShoppingCart.objects.get(user=cart.user,product=item).quantity
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
        context={'items': temp, 'subtotal': subtotal, 'total': total, 'shipping': shipping}
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

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import SubmitRequestForm

def submit_request(request, pk):
    req=get_object_or_404(Request, pk = pk)


    # Create a form instance and populate it with data from the request (binding):
    form = SubmitRequestForm(request.POST)

    # Check if the form is valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        req.request_title = form.cleaned_data['product_name']
        req.request_text = form.cleaned_data['description']
        req.popularity = 0;

        #TODO: make a template for request confirmation
        return HttpResponseRedirect(reverse('requests') )

    return render(request, 'catalog/request_receieved_confirmation.html', {'form': form, 'req':req})


def faq(faq):
     return render(
        faq,
        'faq.html'
    )
