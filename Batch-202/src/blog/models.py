from django.db import models
from django.utils import timezone

# Create your models here.
# auth.user is a model from django.contrib
# many to one

class Post(models.Model):
	author = models.ForeignKey('auth.user')
	email = models.EmailField(max_length=20,null=True,blank=True)  # database and form both can be null.
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)  # blank=True - Form,# null = True - database


 	def publish(self):
 		self.published_date = timezone.now()
 		self.save()

 	def __str__(self):     # __str__ or __unicode__
 		return self.title


# Many to many example
# https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/

from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


 # one to one example

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)