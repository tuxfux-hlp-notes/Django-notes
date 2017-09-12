from django.conf.urls import include, url
from .views import Hello


urlpatterns = [
    url(r'^$', Hello, name='Hello'),
]