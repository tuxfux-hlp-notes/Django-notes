from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from blog.forms import ContactForm

# Create your views here.
def Hello(request):
	return HttpResponse("Hello!!! world - welcome to my first blog !!\n")

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

def contact(request):
	form_class = ContactForm  # class not a instance
	context = {'form':form_class}
	return render(request,'blog/contact.html',context)

