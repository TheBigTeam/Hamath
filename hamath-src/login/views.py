from django.shortcuts import render
from django.template.response import TemplateResponse
from login.models import Login
#from django.contrib.auth import authenticate, login

def index(request):


	#var = 'server variable'                           # send python variable to client from server

	# django.com/en/ref/1.9/models/querysets/

	users = Login.objects.all()                       # get [query set] from db with Object Relational Mapper (ORM)
	#users = Login.objects.filter(first_name='Alan')   # get [filtered query set] from db
	
	#user = Login.objects.get(first_name='Alan')       # query one [object] from db
	user = Login.objects.get(pk=2)                    # query one [primary key object] from db


	return TemplateResponse(request, 'login/index.html', { "users" : users, "user" : user })

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