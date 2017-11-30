from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import ContactForm,BlogForm
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
	# POST and NOT VALID DATA.
		else:
			context = {'form':contact_form}
	# GET 
	return render(request,'blog/ContactForm.html',context)


# day 11
def BlogView(request):
	# POST
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			author = form.cleaned_data['author']
			title = form.cleaned_data['title']
			text = form.cleaned_data['text']
			created_date = form.cleaned_data['created_date']
			published_date = form.cleaned_data['published_date']
			Post.objects.create(author=author,title=title,text=text,created_date=created_date,published_date=published_date)
			return HttpResponseRedirect('/blog/thankyou')
		else:
			context = {'form':form}
			return render(request,'blog/BlogForm.html',context)
	#GET
	else:
		form = BlogForm
		context = {'form':form}
		return render(request,'blog/BlogForm.html',context)




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

