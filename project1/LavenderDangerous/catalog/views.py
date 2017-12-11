from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.contrib.auth.models import User
from .models import Product, Profile, ShoppingCart, Request, Review, Category
import re

def index(index):
    return render(
        index,
    	'index.html'
    )

class ProductListView(generic.ListView):
    model = Product
    checks = []
    search = ''
    def get_queryset(self):
        self.search = self.request.GET.get('q','')
        self.search =re.escape(self.search)
        if len(self.checks)==0:
            return Product.objects.filter(name__icontains=self.search)
        else:
            return Product.objects.filter(category__in=self.checks).all().filter(name__icontains=self.search)
        
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['search'] = self.search
        context['checks'] = self.checks
        return context
        
    def post(self, request, *args,**kwargs):
        self.checks = request.POST.getlist('checks[]')
        return generic.ListView.get(self, request, *args, **kwargs)
        
from .forms import SubmitReviewForm
class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        form = SubmitReviewForm()
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['rvw'] = Review.objects.filter(product_id=self.kwargs['pk']).all()
        context['form'] = form
        return context
        
    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['added'] = ""
        if request.POST.get('review') == 'review':
            form = SubmitReviewForm(self.request.POST)
             # Check if the form is valid:
            if form.is_valid():
                 # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                rting = form.cleaned_data['rating']
                text = form.cleaned_data['review_text']
                prod = Product.objects.get(id=self.kwargs['pk'])
                new_entry = Review(user=self.request.user,product=prod,rating=rting,review_text=text)
                new_entry.save()
        else:
            form = SubmitReviewForm()
            prod = Product.objects.get(id=self.kwargs['pk'])
            inCart = ShoppingCart.objects.filter(user=request.user,product=prod)
            if not inCart:
                s = ShoppingCart(user=request.user,product=prod,quantity=int(request.POST.get('quant')))
                s.save()
                context['added'] = "Added to cart"
            else:
                context['added'] = "Already in cart"
        context['rvw'] = Review.objects.filter(product_id=self.kwargs['pk']).all()
        context['form'] = form
        return self.render_to_response(context=context)

from math import floor
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
@register.simple_tag()
def multiply(x, y, *args, **kwargs):
    return x*y

def cart(request):
    if request.method == "POST":
        item = Product.objects.get(name = request.POST.get('itemchange'))
        if request.POST.get('rm') == 'rm':
            ShoppingCart.objects.filter(user=request.user,product=item).delete()
        else:
            ShoppingCart.objects.filter(user=request.user,product=item).update(quantity=int(request.POST.get('quant')))
    temp = []
    quants = {}
    if request.user.is_authenticated:
        items = ShoppingCart.objects.filter(user=request.user)
        if items != None:
            subtotal = 0
            for item in items:
                item=item.product
                temp.append(item)
                q = ShoppingCart.objects.get(user=request.user,product=item).quantity
                subtotal += item.price*q
                quants[item] = q
            shipping=3.99
            subtotal = round(subtotal, 2)
            total=round((shipping+subtotal),2)
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
        request,
        'cart.html',
        context={'items': temp, 'quants': quants, 'subtotal': subtotal, 'total': total, 'shipping': shipping, 'range': range(1,10)}
    )

def user(request):
    if request.user.is_authenticated:
        temp = []
        items = ShoppingCart.objects.filter(user=request.user)
        if items != None:
            for item in items:
                item=item.product
                temp.append(item)
        else:
            items=None
            
        reqs = Request.objects.filter(user=request.user)
    
        return render(
            request,
            'user.html',
            context={'items': temp,'reqs':reqs}
        )
    else:
        return render(
        request,
    	'index.html'
        )


from .forms import SubmitRequestForm

def requests(request):
    if request.method == 'POST':
        if request.POST.get('pop') == 'pop':
            req = Request.objects.filter(request_title=request.POST.get('rtitle')).first()
            req.popularity+=1
            req.save()
        else:
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
