from django.shortcuts import render
from django.http import HttpResponse

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
def testdata(request):
	context = { 'namesdb': [{'name':'arjouth','blogname':'arjouth first blog','message':'Today is friday.'},
				{'name':'deepthi','blogname':'deepthi first blog','message':'Today is friday.'},
				{'name':'govardan','blogname':'govardhan first blog','message':'Today is friday.'},
				{'name':'ramanji','blogname':'','message':'Today is friday.'}
				]}
	return render(request,'testdata.html',context)	
