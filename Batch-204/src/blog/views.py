from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
	return HttpResponse("Hello!!! world - welcome to my first blog !!\n")

