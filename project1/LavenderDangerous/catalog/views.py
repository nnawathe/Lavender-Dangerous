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
    
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import SubmitRequestForm

def requests(request):
    if request.method == 'POST':
        form = SubmitRequestForm(request.POST)
     # Check if the form is valid:
        if form.is_valid():
         # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            title = form.cleaned_data['product_name']
            text = form.cleaned_data['description']
            pop = 0;
            new_entry = Request(user=request.user,request_title=title,request_text=text,popularity=pop)
            new_entry.save()
    form = SubmitRequestForm()
    num_requests=Request.objects.count()
    rquests=Request.objects.order_by('-popularity').all()

    return render(
    	request,
    	'requests.html',
    	context={'num_requests':num_requests, 'rquests': rquests, 'form':form}
    )


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Request

class RequestCreate(CreateView):
    model = Request
    fields = '__all__'


def faq(faq):
     return render(
        faq,
        'faq.html'
    )
def terms(terms):
    return render(
    terms,
    'terms.html'
    )
