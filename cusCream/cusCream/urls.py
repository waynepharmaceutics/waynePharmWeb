from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cusCream.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #######################SELECTING PRODUCTS AND OVERALL WEB################
    (r'^$', TemplateView.as_view(template_name = 'creamUsers/index.html')),
    (r'^about/', TemplateView.as_view(template_name = 'creamUsers/about.html')),
    (r'^contact/', TemplateView.as_view(template_name = 'creamUsers/contact.html')),
    (r'^plan/', TemplateView.as_view(template_name = 'creamUsers/plan.html')),
    url(r'^build/', TemplateView.as_view(template_name = 'creamUsers/build.html')),
    url(r'^admin/', include(admin.site.urls)),
    
    #################DECIDING PRODUCTS AND CARTS##############################
    url(r'^users/', include('creamUsers.urls', namespace="creamUsers")),
    
    ######################RELATED TO LOGGING IN###############################
    url(r'^register/$', 'creamUsers.views.CreamUserRegistration'),
    url(r'^login/$', 'creamUsers.views.LoginRequest'),
    url(r'^logout/$', 'creamUsers.views.LogoutRequest'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset', name = 'password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name = 'password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name = 'password_reset_complete'),

)
