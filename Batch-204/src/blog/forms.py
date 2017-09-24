from django import forms
from .models import Post

class ContactForm(forms.Form):
	contact_name = forms.CharField(max_length=5,required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		widget = forms.Textarea
		)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author','title','text')