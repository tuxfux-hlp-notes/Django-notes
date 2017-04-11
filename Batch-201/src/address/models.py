from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.8/topics/db/models/#field-types
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
# If you dont define a primary key by default, you will get an autoincremented key value.

# Day 5 - Modifying a field and adding a new field in the databases.
class Address_Detail(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=20,primary_key=True)
	gender = models.CharField(max_length=6,null=True,blank=True)  # null is for databases,blank is for the forms.

# https://docs.djangoproject.com/en/1.8/topics/db/models/#extra-fields-on-many-to-many-relationships

# Day 5 - want to see email and name simultaneously.
# Modification done here are reflected exactly the same in the admin page location.
	def __unicode__(self):
		return u'name:{} - email:{}'.format(self.name,self.email)

class New_Course(models.Model):
	email = models.ForeignKey(Address_Detail)
	course = models.CharField(max_length=30)

	def __unicode__(self):
		return u'email:{} - course:{}'.format(self.email,self.course)




# Day 8
# model forms: https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/


# https://docs.djangoproject.com/en/1.11/topics/db/models/#module-django.db.models
# Advanced Models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# https://docs.djangoproject.com/en/1.11/topics/db/examples/



# example - one to one.
# https://docs.djangoproject.com/en/1.11/topics/db/examples/one_to_one/

class Place(models.Model):                        #  primary table.
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):                  # secondary table.
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

# one to many kinda - not defined in django.
class Waiter(models.Model):                       # secondary tables
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)


# employee - chiru(primary)  - chiru moved away.  -> number of employees - 1
# HR details - primary(one to one) - enabled.
# Payroll details - primary(one to one) on_delete=models.CASCADE,- chiru entries in payroll delted.

# example - Many to one.
# Many reporters working on a single article.
# https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/


class Reporter(models.Model):    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

# https://docs.djangoproject.com/en/1.11/ref/models/options/#model-meta-options
    class Meta:
        ordering = ('pub_date',)


# example - many to many
# https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Articles(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


# TODO
# not to delete the forieng values when we delete the primary.
# ORM.
# changing the database.
# django shell.
# how to enter fake data into tables.
# changing the table in models and managing the data. - TODO

