from django.conf.urls import include, url
from .views import StaticHello


urlpatterns = [
     url(r'^testme/', StaticHello, name='StaticHello'),
]