from django.shortcuts import render

# Create your views here.

def address_test(request):
	context = {}
	return render(request,'address/new_address.html',context)


def blog_test(request):
	context = {}
	return render(request,'address/test_boot.html',context)