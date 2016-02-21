from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from hamath import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

@login_required
def Teacher(request):
	next = request.GET.get('next', settings.TEACHER_URL)
	if is_teacher(request.user):
		return render(request, 'teacher/teacher.html', {})
	else:
		return HttpResponseRedirect('access_denied')

def AccessDenied(request):
    return render(request, 'teacher/access_denied.html', {})