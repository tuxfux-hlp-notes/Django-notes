from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'blog.views.hello_world', name='hello'),
    url(r'^test/', 'blog.views.test_html', name='testhello'),
    url(r'^address/','blog.views.address',name='address')
]
