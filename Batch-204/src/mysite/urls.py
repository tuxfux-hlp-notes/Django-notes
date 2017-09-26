from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^hello/', 'blog.views.Hello', name='Hello'),   # i want all the blog urls to be managed seperately
    #url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^check/', include('check_app.urls')),
]
