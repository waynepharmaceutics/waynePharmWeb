from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from creamUsers import views

urlpatterns = patterns('',
	#########################RELATED TO BUILDLING CREAM#######################
	#url(r'^$', views.UserProfile, name='userInfo'),
	(r'^$', TemplateView.as_view(template_name = 'creamUsers/userInfo.html')),
	url(r'select/$', views.selectAnswers, name='selectAnswer'),
	url(r'^(?P<product_id>\d+)/(?P<answer_id>\d+)/result$', views.result, name='result'),
	url(r'^(?P<product_id>\d+)/result$', views.resultNoAnswer, name='resultNoAnswer'),
	url(r'^(?P<product_id>\d+)/edit$', views.editProd, name='editProd'),
	url(r'^(?P<product_id>\d+)/saveEditResult$', views.saveEditResult, name='saveEditResult'),
	
	########################RELATED TO CHANGING CARTS#########################
	url(r'^cart/$', views.Cartdetail, name = 'cartdetail'),
	url(r'^(?P<product_id>\d+)/add/$', views.AddProduct, name = 'addproduct'),
	url(r'^(?P<product_id>\d+)/plus/$', views.Plusone, name = 'plus'),
	url(r'^(?P<product_id>\d+)/minus/$', views.Minusone, name = 'minus'),
	url(r'^(?P<product_id>\d+)/remove/$', views.Removeproduct, name = 'remove'),
	
	########################RELATED TO PAYPAL OPERATIONS#######################
	url(r'^checkout/$', views.checkOutWithPaypal, name = 'checkout'),
	
)