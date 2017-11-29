from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

#day7
# integrating models to the templates.
def myblog(request):
	blog_data = Post.objects.all()
	context = {'namesdb': blog_data}
	return render(request,'blog/myblog.html',context)

#day9
# creating a contact form
# https://docs.djangoproject.com/en/1.11/topics/forms/#the-view
# https://docs.djangoproject.com/en/1.11/ref/forms/api/#django.forms.Form.cleaned_data
# https://docs.djangoproject.com/en/1.11/topics/email/
def ContactView(request):

	# GET
	contact_form = ContactForm  # class not a instance.
	context = {'form':contact_form}
	
	# POST
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
	# POST and VALID data.
		if contact_form.is_valid():
			contact_name = contact_form.cleaned_data['contact_name']
			contact_email = contact_form.cleaned_data['contact_email']
			content = contact_form.cleaned_data['content']
			subject = "A new contact or lead - {}".format(contact_name)
			email = EmailMessage(subject,contact_name + '\n' + contact_email + '\n' + content , to=['tuxfux.hlp@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thankyou/')
	# GET or POST and NOT VALID DATA.
	return render(request,'blog/ContactForm.html',context)

#day10
def Thanks(request):
	return HttpResponse("Thank you for contacting us !!!")

# day2
# def hello_world(request):
# 	return HttpResponse("Hello!! world \n")

# day3
# def hello_world(request):
# 	f = open('/home/khyaathi/Documents/tuxfux-hlp-notes/Django-notes/Batch-205/src/blog/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)

# day3
# https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
# templates folder in app locations.
def hello_world(request):
	context = {}
	return render(request,'test.html',context)

# # day4
# def myblog(request):
# 	context = {'namesdb':[{'name':'Ravi','course':'Django','loc':'India'},{'name':'rama','course':'django','loc':'Us'}]}
# 	return render(request,'blog/myblog.html',context)

