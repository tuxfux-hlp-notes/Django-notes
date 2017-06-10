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

# form for your posts
# https://docs.djangoproject.com/en/1.11/ref/models/options/

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','email','title','text','created_date',)
		#fields = ('title','text',)
