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