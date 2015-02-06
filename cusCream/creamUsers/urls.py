from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from creamUsers import views

urlpatterns = patterns('',
	#########################RELATED TO BUILDLING CREAM#######################
	#url(r'^$', views.UserProfile, name='userInfo'),
	(r'^$', TemplateView.as_view(template_name = 'creamUsers/userInfo.html')),
	url(r'select/$', views.selectAnswers, name='selectAnswer'),
	url(r'^(?P<product_id>\d+)/(?P<answer_id>\d+)/result$', views.result, name='result'),
	
	########################RELATED TO CHANGING CARTS#########################
	
)