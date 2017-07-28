from django.conf.urls import include, url
<<<<<<< HEAD
from .views import hello_world,test_hello,blogdata,contact,thanks,Bloginsert
=======
from .views import hello_world,test_hello,testdata,contact,thanks,Bloginsert
>>>>>>> ac0f006f4559b51ce969a472938dff242797d9c6

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello_world, name='home'),
    url(r'^test/', test_hello, name='testhome'),
<<<<<<< HEAD
    url(r'^blogdata/', blogdata, name='blogdata'), # changed the name from testdata to blogdata
=======
    url(r'^testdata/', testdata, name='testdata'),
>>>>>>> ac0f006f4559b51ce969a472938dff242797d9c6
    url(r'^contact/',contact,name='contact'),  # form
    url(r'^post/',Bloginsert,name='blog'),     # form
    url(r'^thanks/',thanks,name='thanks'),     # thank you redirect
]