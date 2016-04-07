from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from hamath import settings
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from student.models import Score

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()

def get_student_score(request):
	if is_teacher(request.user):

		group = Group.objects.get(name='Student')
		students = group.user_set.all()
		# scores = 
		return { 'students' : students }
	else:
		return None

@login_required
def Teacher(request):
	if is_teacher(request.user):
		context = get_student_score(request)
		return render(request, 'teacher/teacher.html', context)
	else:
		return HttpResponseRedirect('access_denied')

def AccessDenied(request):
    return render(request, 'teacher/access_denied.html', {})