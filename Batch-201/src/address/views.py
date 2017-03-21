from django.shortcuts import render
from django.http import HttpResponse
from AddressBook.settings import BASE_DIR
from .models import Address_Detail
from .forms import ContactForm

# Day2 
# Create your views here.

# def hello_world(request):
# 	return HttpResponse("Hello!! world \n")


# # Not how we do in django.
# # This is more of a pythonic way.
# def test_hello(request):
# 	#f = open('/home/key2gyaan/Documents/git_repositories/tuxfux-hlp-notes/Django-notes/Batch-201/src/address/templates/test.html')
# 	f = open(BASE_DIR + '/address/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)

# using render instead of the above method
# make sure your app - address is added to the INSTALLED_APPS  inside the setting.py file.
# def test_hello(request):
# 	context = {}
# 	return render(request,'test.html',context)

# Day3 

# static page display for address.html
# def address(request):
# 	context = {}
# 	return render(request,'address.html',context)

# def Daddress(request):
# 	context={'name1':'student1','email1':'tuxfux.hlp@gmail.com','name2':'student2','email2':'tuxfux.hlp@edu.com','addr1':''}
# 	return render(request,'Daddress.html',context)

# def Daddress(request):
# 	context = {'namesdb':[{'name':'student1','email':'tuxfux.hlp@gmail.com'},{'name':'student2','email':'tuxfux.hlp@edu.com'}]}
# 	return render(request,'Daddress.html',context)

# def Naddress(request):
# 	context = {'namesdb':[{'name':'student1','email':'tuxfux.hlp@gmail.com'},{'name':'student2','email':'tuxfux.hlp@edu.com'}]}
# 	return render(request,'address.html',context)

# Day 4
# trying to integrate the template with the database.
def Naddress(request):
	#context = {'namesdb':[{'name':'student1','email':'tuxfux.hlp@gmail.com'},{'name':'student2','email':'tuxfux.hlp@edu.com'}]}
	values = Address_Detail.objects.all()
	context = {'namesdb':values}
	return render(request,'address/address.html',context)

# Day 7
# creation of a contact page

def contact(request):
	form_class = ContactForm  # form_class is an instance of our contact form.
	context = {'form':form_class}
	return render(request,'address/contact.html',context)


