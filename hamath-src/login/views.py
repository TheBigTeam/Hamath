from django.shortcuts import render
from django.template.response import TemplateResponse
from login.models import Login
from django.contrib.auth import authenticate, login

def index(request):

	#value = Login.objects.all()
	value = '[Login] from the server'
	return TemplateResponse(request, 'login/index.html', { "key" : value })

'''
def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return TemplateResponse(request, 'student/index.html', {})
		else:
			return 'error: disabled account'

	else:
		return 'error: invalid login'
'''