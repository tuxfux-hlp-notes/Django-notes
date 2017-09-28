from django.conf.urls import include, url
#from .views import Hello,TestHello,StaticHello
from .views import StaticHello
from .views import contact,Thanks,BlogInsert,BlogData,home


urlpatterns = [
    url(r'^blogdata', BlogData, name='blogdata'),
    url(r'^$', home, name='home'),
    # url(r'^test/', TestHello, name='Hello'),
    url(r'^testme/', StaticHello, name='StaticHello'),
    url(r'^contactme/',contact,name='contact'),
    url(r'^thanks/',Thanks,name='thanks'),
    url(r'^post/',BlogInsert,name='blog')
]