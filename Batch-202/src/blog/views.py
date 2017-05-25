from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based views.
# class based views.

# views
# https://docs.djangoproject.com/en/1.8/topics/http/views/

def hello_world(request):
	return HttpResponse("hello world \n")
