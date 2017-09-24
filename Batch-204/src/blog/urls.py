from django.conf.urls import include, url
#from .views import Hello,TestHello,StaticHello
from .views import contact,Thanks,BlogInsert,BlogData


urlpatterns = [
    url(r'^$', BlogData, name='blogdata'),
    # url(r'^test/', TestHello, name='Hello'),
    # url(r'^testme/', StaticHello, name='StaticHello'),
    url(r'^contact/',contact,name='contact'),
    url(r'^thanks/',Thanks,name='thanks'),
    url(r'^post/',BlogInsert,name='blog')
]