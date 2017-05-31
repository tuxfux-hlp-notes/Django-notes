from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.post_list,name='post_list'),
	url(r'^hello/', views.hello_world, name='hello'),
    url(r'^test/', views.test_html, name='testhello'),
    url(r'^address/',views.address,name='address'),
]

