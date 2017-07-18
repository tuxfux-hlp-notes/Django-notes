from django.conf.urls import include, url
from .views import hello_world,test_hello,testdata

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello_world, name='home'),
    url(r'^test/', test_hello, name='testhome'),
    url(r'^testdata/', testdata, name='testdata'),
]