from django.shortcuts import render
from django.http import HttpResponse
from mysite.settings import BASE_DIR

# Create your views here.
# function based views.
# class based views.

# views
# https://docs.djangoproject.com/en/1.8/topics/http/views/

def hello_world(request):
	return HttpResponse("hello world \n")

# day 3 - one way of displaying the contents of the template.
# def test_html(request):
# 	f = open( BASE_DIR + '/blog/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)


def test_html(request):
	context = {}
	return render(request,'test.html',context)