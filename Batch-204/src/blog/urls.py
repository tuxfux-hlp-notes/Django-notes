from django.conf.urls import include, url
from .views import Hello,TestHello,StaticHello
from .views import contact,Thanks


urlpatterns = [
    url(r'^$', Hello, name='Hello'),
    url(r'^test/', TestHello, name='Hello'),
     url(r'^testme/', StaticHello, name='StaticHello'),
     url(r'^contact/',contact,name='contact'),
      url(r'^thanks/',Thanks,name='thanks'),
]