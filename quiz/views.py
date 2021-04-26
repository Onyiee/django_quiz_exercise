from django.shortcuts import render
from quiz.models import Question


# Create your views here.
def display(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'quiz/home.html', context)


def submit(request):
    return render(request, 'quiz/submit_page.html')