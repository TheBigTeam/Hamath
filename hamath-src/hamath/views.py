from django.shortcuts import render
from django.contrib.auth.models import User
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
            return TemplateResponse(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm()
        return TemplateResponse(request, 'signup.html', {'form': form})


def Login(request):
    next = request.GET.get('next', settings.STUDENT_URL)
    if request.user.is_authenticated():
            return HttpResponseRedirect(settings.STUDENT_URL)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return TemplateResponse(request, 'login.html', {'form': form})
        else:
            return TemplateResponse(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
        return TemplateResponse(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.HOME_URL)

"""
broken
"""
"""
class StudentView(View):
    @login_required
    def get(self, request):
        return render(request, 'student.html', {})
"""     

@login_required
def Student(request):
    return render(request, 'student.html', {})

class HomeView(TemplateView):
    template_name = 'home.html'