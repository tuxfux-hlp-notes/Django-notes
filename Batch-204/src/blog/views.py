from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage

from .models import Post
from blog.forms import ContactForm

# Create your views here.
def Hello(request):
	return HttpResponse("Hello!!! world - welcome to my first blog !!\n")

# Thank you
def Thanks(request):
	return HttpResponse("Thank you and Have a great day!!!")


# task 1
# how to use the BASE_DIR to read your test.html without giving full path.
# def TestHello(request):
# 	f = open('/home/khyaathi/Documents/tuxfux-hlp-notes/Django-notes/Batch-204/src/blog/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)

# def TestHello(request):
# 	context = {'blogdb':[{'title':'My first blog - manindra','content':'Hey there i am learning about Deploying the admin',
# 				'author':'Manindra'},{'title':'My first blog - anu','content':'Hey there i am tryingt to learn tags',
# 				'author':'anu'}]}
# 	return render(request,'test.html',context)

def TestHello(request):
	context = {'blogdb': Post.objects.all() }    # select * from post;
	return render(request,'test.html',context)

def StaticHello(request):
	context = {}
	return render(request,'blog/static_test.html',context)

# https://docs.djangoproject.com/en/1.11/topics/forms/#the-view
# https://docs.djangoproject.com/en/1.11/ref/forms/api/#django.forms.Form.cleaned_data
# https://docs.djangoproject.com/en/1.11/topics/email/
def contact(request):

	# GET REQUEST
	form_class = ContactForm  # class not a instance
	context = {'form':form_class}
    
    # POST REQUEST
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			content = form.cleaned_data['content']
			subject = "A new contact or lead - {}".format(contact_name)
			email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + content , to=['tuxfux.hlp@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thanks/')			
	return render(request,'blog/contact.html',context)

