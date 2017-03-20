from django.shortcuts import render

# Create your views here.

def Taddress(request):
	context = {}
	return render(request,'newtest_app/test.html',context)
