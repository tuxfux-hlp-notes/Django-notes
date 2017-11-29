from django.conf.urls import include, url
from .views import ContactView,Thanks

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','blog.views.myblog',name='myblog'),
    url(r'^contact/',ContactView,name='contact'),
    url(r'^thankyou/',Thanks,name='thanks')
]
