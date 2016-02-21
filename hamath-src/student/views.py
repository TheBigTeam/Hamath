from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Student(request):
    return render(request, 'student/student.html', {})

@login_required
def GetScores(request):
	return render(request, 'student/menu/get_scores.html', {})

@login_required
def HowToPlay(request):
	return render(request, 'student/menu/how_to_play.html', {})


"""
class StudentView(View):
    @login_required
    def get(self, request):
        return render(request, 'student.html', {})
"""     