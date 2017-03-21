from django import forms

# Day 7
# fields: https://docs.djangoproject.com/en/1.8/ref/forms/fields/
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
			required = True,
			widget = forms.Textarea)