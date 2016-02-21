from django.shortcuts import render
from django.contrib.auth.models import User, Group #use group to authenticate teachers during signup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from hamath.forms import RegistrationForm, LoginForm
from hamath.models import Student
from hamath import settings

from django.views.generic.base import View, TemplateView

def SignUp(request):
    next = request.GET.get('next', settings.LOGIN_URL)
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.HOME_URL)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'].title(), 
                last_name=form.cleaned_data['last_name'].title(),
                email=form.cleaned_data['email'], 
                password=form.cleaned_data['password']
            )
            user.save()
            return HttpResponseRedirect(next)
        else:
            return TemplateResponse(request, 'hamath/signup.html', {'form': form})
    else:
        form = RegistrationForm()
        return TemplateResponse(request, 'hamath/signup.html', {'form': form})


def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()


def student_teacher_redirect(request):
    if is_teacher(request.user):
        return render(request, 'teacher/teacher.html', {})
    else:
        return render(request, 'student/student.html', {})


def Login(request):
    if request.user.is_authenticated():
        student_teacher_redirect(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        else:
            return TemplateResponse(request, 'hamath/login.html', {'form': form})

        if user is not None:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect(settings.STUDENT_URL)
                return student_teacher_redirect(request)
            else:
                return TemplateResponse(request, 'hamath/login.html', {'form': form})
        else:
            return TemplateResponse(request, 'hamath/login.html', {'form': form})

    else:
        form = LoginForm()
        return TemplateResponse(request, 'hamath/login.html', {'form': form})


def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.HOME_URL)


class HomeView(TemplateView):
    template_name = 'hamath/home.html'


def About(request):
    return render(request, 'hamath/about.html', {})


def Contact(request):
    return render(request, 'hamath/contact.html', {})