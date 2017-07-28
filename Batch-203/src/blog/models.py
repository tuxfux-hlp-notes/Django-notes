from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True) # blank=True - Form,null=True - database
	email = models.EmailField(max_length=30,blank=True,null=True)

	def publish(self):
	 	self.published_date = timezone.now()
	 	self.save()

	def __str__(self):    # __str__ or __unicode__
		return "{} {} {}".format(self.author,self.title,self.text)