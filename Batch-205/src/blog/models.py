from django.db import models
from django.utils import timezone

# Create your models here.

# day7 : Adding a email field
# https://docs.djangoproject.com/en/1.11/ref/models/fields/#emailfield

# Many to one relationship
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


###
# one to one relationship.
###

# from django.db import models

# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)

#     def __str__(self):
#         return "%s the place" % self.name

# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)

#     def __str__(self):
#         return "%s the restaurant" % self.place.name

# class Waiter(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return "%s the waiter at %s" % (self.name, self.restaurant)


###
# Many to Many relationship.
###

# from django.db import models

# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ('title',)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ('headline',)


## 
# Many to one example.

# from django.db import models

# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)  # unique

#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ('headline',)
