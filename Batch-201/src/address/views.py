from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AddressBook.settings import BASE_DIR
from .models import Address_Detail
from .forms import ContactForm, AddressForm
from django.core.mail import EmailMessage
from django.utils.translation import ugettext as _


# day 10
# creating our home page
def home(request):
    context = {}
    return render(request, 'home.html', context)


# Modular views
# class based views : https://docs.djangoproject.com/en/1.10/topics/class-based-views/


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
    # context = {'namesdb':[{'name':'student1','email':'tuxfux.hlp@gmail.com'},{'name':'student2','email':'tuxfux.hlp@edu.com'}]}
    values = Address_Detail.objects.all()
    context = {'namesdb': values}
    return render(request, 'address/address.html', context)


# Day 7
# creation of a contact page
# https://docs.djangoproject.com/en/1.10/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

def contact(request):
    form_class = ContactForm  # form_class is an instance of our contact form.
    context = {'form': form_class}  # {'form': <class 'address.forms.ContactForm'>}

    # request method are of two types - POST METHOD and GET METHOD.
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print dir(form)
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            subject = "A new contact or lead - {}".format(contact_name)
            print contact_name, contact_email, content, subject
            email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + content,
                                 to=['tuxfux.hlp@gmail.com'])
            email.send()
            return HttpResponseRedirect('/thankyou/')
        # request method is GET please open the same contact page.
    return render(request, 'address/contact.html', context)


# Day 8
# modular forms
# https://docs.djangoproject.com/en/1.10/ref/forms/validation/#form-and-field-validation
def address_form(request):
    form = AddressForm()
    context = {'form': form}

    if request.method == 'POST':
        # POST and FORM=VALID
        form = AddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            # ORM related entry to create a new object
            Address_Detail.objects.create(name=name, email=email, gender=gender)
            return HttpResponseRedirect('/thankyou/')
        else:
            # POST and FORM=INVALID
            print request.method
            # print form.errors
            print form
            context = {'form': form}
            return render(request, 'address/Address_form.html', context)
    # GET
    return render(request, 'address/Address_form.html', context)


def thank_you(request):
    return HttpResponse("Thank you for contacting us.")


def bootme(request):
    return render(request, 'address/bootme.html', {})


# internationalization and Localization
def my_function(request):
    output = _("welcome to my site.")
    return render(request, "localize/my_testing.html", {'output': output})
