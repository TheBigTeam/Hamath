from django.shortcuts import render
from django.template.response import TemplateResponse
from login.models import Login

# Create your views here.

def index(request):

	#value = Login.objects.all()
	value = 'from the server'
 	
	return TemplateResponse(request, 'login/index.html', { "key" : value })