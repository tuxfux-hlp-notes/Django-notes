from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.address_test,name='address_test'),
	url(r'^blog/',views.blog_test,name='blog_test')
]
