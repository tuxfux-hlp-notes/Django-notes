from django import forms
from .models import Post

class ContactForm(forms.Form):
	contact_name = forms.CharField(max_length=20,required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		widget = forms.Textarea
		)

# https://docs.djangoproject.com/en/1.11/ref/models/options/
class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		#fields = ['author','title','text','created_date']
		fields = '__all__'


	# form validation
	def clean_email(self):
		email = self.cleaned_data.get('email')  # the email field is in relation to model.py(Post class)
		print email

		if email:
			(ename,edomain) = email.split('@')
			if edomain != 'khyaathi.com':
				raise forms.ValidationError("please try to enter a valid khyaathi email address.")
		return email