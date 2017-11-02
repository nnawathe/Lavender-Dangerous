from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'user', views.user, name='user'),
	url(r'cart', views.cart, name='cart'),
	url(r'faq', views.faq, name='faq'),
	url(r'requests', views.requests, name='requests'),
    url(r'product', views.product, name='product'),
	# url(r'product', views.ProductListView.as_view(), name='product'),
]
