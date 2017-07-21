from django.shortcuts import render

# Create your views here.

def testdata(request):
	context = { 'newdb': [{'name':'arjouth-a','blogname':'arjouth first blog','message':'Today is friday.'},
				{'name':'deepthi-a','blogname':'deepthi first blog','message':'Today is friday.'},
				{'name':'govardan-a','blogname':'govardhan first blog','message':'Today is friday.'},
				{'name':'ramanji-a','blogname':'','message':'Today is friday.'}
				]}
	return render(request,'test_app/testdata.html',context)	
