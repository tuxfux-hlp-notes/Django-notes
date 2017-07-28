from django.conf.urls import include, url
from django.contrib import admin
#from django.conf import settings
from mysite.settings import DEBUG

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),   # django admin app.
    url(r'^$','blog.views.home',name='home'),
    url(r'^blog/',include('blog.urls')),         # blog app
    url(r'^address/',include('address.urls')),         # address app
    url(r'^accounts/', include('registration.backends.default.urls')), # django registartion redux
]

print DEBUG
if DEBUG:  # when DEBUG is set to TRUE
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

