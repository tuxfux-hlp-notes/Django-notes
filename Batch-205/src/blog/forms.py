from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(max_length=20,required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		widget = forms.Textarea
		)