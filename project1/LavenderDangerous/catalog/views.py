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
        form = SubmitReviewForm(self.request.POST)
         # Check if the form is valid:
        if form.is_valid():
             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            rting = form.cleaned_data['rating']
            text = form.cleaned_data['review_text']
            prod = Product.objects.get(id=self.kwargs['pk'])
            new_entry = Review(user=self.request.user,product=prod,rating=rting,review_text=text)
            new_entry.save()
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['rvw'] = Review.objects.filter(product_id=self.kwargs['pk']).all()
        context['form'] = form
        return self.render_to_response(context=context)

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
