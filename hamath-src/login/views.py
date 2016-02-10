from django.shortcuts import render
#from django.http import HttpResponse
from django.template.response import TemplateResponse
from login.models import Login

# Create your views here.

def index(request):
	#return HttpResponse("Hello Django")

	data = Login.objects.all()

	# returning raw data from the server
	title = 'login page'

	return TemplateResponse(request, '/Users/aidanmelen/Developer/hammath-workspace/hamath-src/login/template/login.html', { "data" : data })