from tastypie.resources import ModelResource

# model information getting imported.
from django.contrib.auth.models import User
from .models import Post

class PostResource(ModelResource):
	class Meta:
		queryset = Post.objects.all()
		resource_name = 'post'

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'