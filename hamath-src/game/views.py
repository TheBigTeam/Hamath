from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def PlayHamath(request):
	return render(request, 'student/menu/choose_difficulty.html', {})

@login_required
def RookieMode(request):
	return render(request, 'student/game/rookie_mode.html', {})

@login_required
def IntermediateMode(request):
	return render(request, 'student/game/intermediate_mode.html', {})

@login_required
def MasterMode(request):
	return render(request, 'student/game/master_mode.html', {})

