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
		fields = ['author','title','text','created_date','published_date']