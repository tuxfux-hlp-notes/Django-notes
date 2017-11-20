from django.db import models
from django.utils import timezone

# Create your models here.

# day7 : Adding a email field
# https://docs.djangoproject.com/en/1.11/ref/models/fields/#emailfield

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	email  = models.EmailField(max_length=30,blank=True,null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True) # null -> databases, blank -> forms

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
