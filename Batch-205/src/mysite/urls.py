from django.conf.urls import include, url
from django.contrib import admin


### the below are for tastypie application
from blog.api import PostResource,UserResource
post_resource = PostResource()
user_resource = UserResource()



urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$','blog.views.home',name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^api/',include(post_resource.urls)),
    url(r'^api/',include(user_resource.urls)),
]
