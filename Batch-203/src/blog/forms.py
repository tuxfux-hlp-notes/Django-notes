from django import forms
from .models import Post

# static forms
class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
			required=True,
			widget = forms.Textarea
		)

# Model form
class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['author','email','title','text','created_date','published_date']

	# form validations
	def clean_email(self):
		email = self.cleaned_data.get('email')
		print email,type(email)

		if email:
			(ename,edomain) = email.split('@')  # deepthi@khyaathi.com
			if edomain != 'khyaathi.com':
				raise forms.ValidationError("Please try to enter a valid khyaathi email address.")
		return email