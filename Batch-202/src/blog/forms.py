from django import forms
from .models import Post

# genric form.
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required = True,
		widget = forms.Textarea
		)

# validation
# clean has to be used before the field. 
# clean_email has to be used.
	def clean_contact_email(self):
		contact_email = self.cleaned_data.get('contact_email')
		(ename,edomain) = contact_email.split('@')
		if edomain != 'khyaathi.com':
			raise forms.ValidationError("please try to enter a valid khyaathi edu mail address")
		return email

# form for your posts
# https://docs.djangoproject.com/en/1.11/ref/models/options/

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','email','title','text','created_date',)
		#fields = ('title','text',)

# validation
# clean has to be used before the field. 
# clean_email has to be used.
	def clean_email(self):
		email = self.cleaned_data.get('email')
		(ename,edomain) = email.split('@')
		if edomain != 'khyaathi.com':
			raise forms.ValidationError("please try to enter a valid khyaathi edu mail address")
		return email