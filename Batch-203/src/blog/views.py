from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def hello_world(request):
	return HttpResponse("Hello!! world \n")

# example 1:
# def test_hello(request):
# 	f = open('/home/khyaathi/Documents/tuxfux-hlp-notes/Django-notes/Batch-203/src/blog/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)


# example 2
def test_hello(request):
	context = {}
	return render(request,'test.html',context)

# example 3 - Django_batch203_day3_notes.txt
# def testdata(request):
# 	context = {'name1':'arjouth-a','blogname1':'arjouth first blog','message1':'Today is friday.'
# 				,'name2':'deepthi-a','blogname2':'deepthi first blog','message2':'Today is friday.'
# 				,'name3':'govardan-a','blogname3':'govardhan first blog','message3':'Today is friday.'}
# 	return render(request,'testdata.html',context)	

# Example 4 - Django_batch203_day4_notes.txt
# def testdata(request):
# 	context = { 'namesdb': [{'name':'arjouth','blogname':'arjouth first blog','message':'Today is friday.'},
# 				{'name':'deepthi','blogname':'deepthi first blog','message':'Today is friday.'},
# 				{'name':'govardan','blogname':'govardhan first blog','message':'Today is friday.'},
# 				{'name':'ramanji','blogname':'','message':'Today is friday.'}
# 				]}
# 	return render(request,'testdata.html',context)	

# example 4 - Django_batch203_day6_notes.txt
def testdata(request):
	values = Post.objects.all()
	context = { 'namesdb':values }
	return render(request,'testdata.html',context)	

def thanks(request):
	return HttpResponse("Thank you and we will get back to you soon. Please go back to the home page.")

### Django_batch203_day8_notes.txt
def contact(request):
	form_class = ContactForm
	context = {'form':form_class}
	### Django_batch203_day9_notes.txt
	print request.method
    # POST
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#print dir(form)
		#print form.is_valid()
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			subject = "A new Contact/Lead for Khyaathi - {}".format(contact_name)
			content = form.cleaned_data['content']
			#print contact_name,contact_email,subject,content
			email = EmailMessage(subject,contact_name + '-' + contact_email + '\n' + content , to=['tuxfux.hlp@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thanks/')
	# GET
	return render(request,'blog/contact.html',context)