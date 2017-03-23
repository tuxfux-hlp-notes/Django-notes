from django import forms
from .models import Address_Detail
import re

# Day 7
# fields: https://docs.djangoproject.com/en/1.8/ref/forms/fields/
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
			required = True,
			widget = forms.Textarea)

# Day 8
# https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
# i want to create a form out of my model data.

class AddressForm(forms.ModelForm):
	class Meta:
			model = Address_Detail
			fields = ['name','email','gender']

# Day 9
# Validation of the form values.
# https://docs.djangoproject.com/en/1.10/ref/forms/api/#accessing-clean-data
# https://docs.djangoproject.com/en/1.10/ref/forms/validation/#form-and-field-validation
# ContactForm - todo search link

	def clean_email(self):
		email = self.cleaned_data.get('email')
		print email
		(ename,edomain) = email.split('@') # kumar@gmail.com => (ename,edomain) = [kumar,gmail.com]
		if edomain != 'edu.com':
			# Lets try to add the crispy forms.. may be this should help us.
			raise forms.ValidationError("Please try to enter a valid .edu domain address")
		return email

	def clean_gender(self):
		gender = self.cleaned_data.get('gender')
		if re.match(gender,'male') or re.match(gender,'female'):
			return gender
		else:
			raise forms.ValidationError("You should be either an male or a female.")

# day 10
# crispy forms
# http://django-crispy-forms.readthedocs.io/en/latest/
# tastypie - RESTAPI
