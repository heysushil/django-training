from django.shortcuts import render

from django.http import HttpResponse

from .models import Question
# Create your views here.

# index is a default function
def index(request):
    latest_question = Question.objects.order_by('-pub_date')
    output = ', '.join([q.question_text for q in latest_question])
    return HttpResponse(output)

# Single question ka detail show karne ke liye method
def detial(request, question_id):
    return HttpResponse("You are looking at the question %s" % question_id)

# Question ke result ko show karnae ke liye method
def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)