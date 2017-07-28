from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import ContactForm,BlogForm
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
# changed the name testdata to blogdata.
def blogdata(request):
	values = Post.objects.all()
	context = { 'namesdb':values }
	return render(request,'testdata.html',context)	

def thanks(request):
	return HttpResponse("Thank you and we will get back to you soon. Please go back to the home page.")

### Django_batch203_day8_notes.txt
def contact(request):
	form = ContactForm
	context = {'form':form}
	### Django_batch203_day9_notes.txt
	print request.method
    
    # POST
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#print dir(form)
		#print form.is_valid()
		# Go into the block if the form is valid.
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			subject = "A new Contact/Lead for Khyaathi - {}".format(contact_name)
			content = form.cleaned_data['content']
			#print contact_name,contact_email,subject,content
			email = EmailMessage(subject,contact_name + '-' + contact_email + '\n' + content , to=['tuxfux.hlp@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thanks/')
		# what if the form is not valid.
		else:
			context = {'form':form}
			return render(request,'blog/contact.html',context)

	# GET
	return render(request,'blog/contact.html',context)

# Model form
### Django_batch203_day10_notes.txt
def Bloginsert(request):
	print request.method
	# POST
	if request.method == 'POST':
		form = BlogForm(request.POST)
		# if form is valid
		print form.is_valid()
		if form.is_valid():
			author = form.cleaned_data['author']
			title = form.cleaned_data['title']
			text = form.cleaned_data['text']
			created_date = form.cleaned_data['created_date']
			published_date = form.cleaned_data['published_date']
<<<<<<< HEAD
			email = form.cleaned_data['email']
			print author,title,text,created_date,published_date
			Post.objects.create(author=author,title=title,text=text,created_date=created_date,published_date=published_date,email=email)
=======
			print author,title,text,created_date,published_date
			Post.objects.create(author=author,title=title,text=text,created_date=created_date,published_date=published_date)
>>>>>>> ac0f006f4559b51ce969a472938dff242797d9c6
			return HttpResponseRedirect('/blog/thanks/')
		# what if the form is not valid.
		else:
			context = {'form':form}
			return render(request,'blog/post.html',context)
	#GET
	else:
			form = BlogForm
			context = {'form':form}
			print form
			return render(request,'blog/post.html',context)



