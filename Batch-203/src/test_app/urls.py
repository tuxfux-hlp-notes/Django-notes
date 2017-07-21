from django.conf.urls import include, url
from .views import testdata

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^testdata/', testdata, name='testdata'),
]