from django.shortcuts import render
#from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
	#return HttpResponse("Hello Django")
	return TemplateResponse(request, '/Users/aidanmelen/Developer/hammath-workspace/hamath-src/login/template/login.html', {})