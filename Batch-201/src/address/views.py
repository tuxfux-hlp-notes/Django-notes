from django.shortcuts import render
from django.http import HttpResponse
from AddressBook.settings import BASE_DIR

# Create your views here.

def hello_world(request):
	return HttpResponse("Hello!! world \n")


# # Not how we do in django.
# # This is more of a pythonic way.
# def test_hello(request):
# 	#f = open('/home/key2gyaan/Documents/git_repositories/tuxfux-hlp-notes/Django-notes/Batch-201/src/address/templates/test.html')
# 	f = open(BASE_DIR + '/address/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)

# using render instead of the above method
# make sure your app - address is added to the INSTALLED_APPS  inside the setting.py file.
def test_hello(request):
	context = {}
	return render(request,'test.html',context)