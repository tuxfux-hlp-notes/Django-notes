from django.conf.urls import include, url
from django.contrib import admin
from .views import ContactView,Thanks,BlogView


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','blog.views.myblog',name='myblog'),
    url(r'^ContactForm/',ContactView,name='contact'),
    url(r'^PostForm/',BlogView,name='blog'),
    url(r'^thankyou/',Thanks,name='thanks'),

]
