from django.conf.urls import include, url
from .views import hello_world,test_hello,blogdata,contact,thanks,Bloginsert


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello_world, name='home'),
    url(r'^test/', test_hello, name='testhome'),
    url(r'^blogdata/', blogdata, name='blogdata'), # changed the name from testdata to blogdata
    url(r'^contact/',contact,name='contact'),  # form
    url(r'^post/',Bloginsert,name='blog'),     # form
    url(r'^thanks/',thanks,name='thanks'),     # thank you redirect
]