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

# Day 8
# model forms: https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/




