from django.shortcuts import render
# use group to authenticate teachers during signup
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from hamath.forms import RegistrationForm, LoginForm
from hamath import settings
from student.models import Score
import teacher

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
            score = Score(
                user=User.objects.get(pk=user.pk),
                rookie=0, 
                intermediate=0, 
                master=0
            )
            user.save()
            score.save()

            student_group = Group.objects.get(name=settings.DEFAULT_GROUP_NAME) 
            student_group.user_set.add(user)
            
            return HttpResponseRedirect(next)
        else:
            return TemplateResponse(request, 'hamath/signup.html', {'form': form})
    else:
        form = RegistrationForm()
        return TemplateResponse(request, 'hamath/signup.html', {'form': form})


def student_teacher_redirect(request):
    if teacher.views.is_teacher(request.user):
        context = teacher.views.get_student_score(request)
        return render(request, 'teacher/teacher.html', context)
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
                # return HttpResponseRedirect(settings.STUDENT_URL)
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
    return render(request, 'hamath/about.html', {'version': settings.VERSION})


def Contact(request):
    return render(request, 'hamath/contact.html', {})


def my_custom_bad_request_view(request):
    return render(request, '400.html', {})


def my_custom_permission_denied_view(request):
    return render(request, '403.html', {})


def my_custom_page_not_found_view(request):
    return render(request, '404.html', {})


def my_custom_error_view(request):
    return render(request, '500.html', {})
