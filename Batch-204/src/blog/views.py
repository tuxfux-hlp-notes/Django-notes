from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
	return HttpResponse("Hello!!! world - welcome to my first blog !!\n")

# task 1
# how to use the BASE_DIR to read your test.html without giving full path.
# def TestHello(request):
# 	f = open('/home/khyaathi/Documents/tuxfux-hlp-notes/Django-notes/Batch-204/src/blog/templates/test.html')
# 	content = f.read()
# 	return HttpResponse(content)

def TestHello(request):
	context = {'title':'My first blog - manindra','content':'Hey there i am learning about Deploying the admin',
				'author':'Manindra'}
	return render(request,'test.html',context)
