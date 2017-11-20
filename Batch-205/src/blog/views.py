from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

#day7
# integrating models to the templates.
def myblog(request):
	blog_data = Post.objects.all()
	context = {'namesdb': blog_data}
	return render(request,'blog/myblog.html',context)

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

