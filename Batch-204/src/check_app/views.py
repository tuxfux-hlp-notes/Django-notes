from django.shortcuts import render

# Create your views here.

def StaticHello(request):
	context = {}
	return render(request,'static_test.html',context)
