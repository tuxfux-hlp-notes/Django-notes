from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
	return HttpResponse("Hello!! world \n")

def test_hello(request):
	f = open('/home/khyaathi/Documents/tuxfux-hlp-notes/Django-notes/Batch-203/src/blog/templates/test.html')
	content = f.read()
	return HttpResponse(content)
