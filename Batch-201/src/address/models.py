from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.8/topics/db/models/#field-types
# If you dont define a primary key by default, you will get an autoincremented key value.

class Address_Detail(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=20,primary_key=True)

# https://docs.djangoproject.com/en/1.8/topics/db/models/#extra-fields-on-many-to-many-relationships
	
	def __unicode__(self):
		return self.name


