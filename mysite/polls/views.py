from django.shortcuts import render

from django.http import HttpResponse
# import django.template.loader as loader
from django.template import loader 
from .models import Question
# Create your views here.

# index is a default function
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # define a html page in whcih you want to share the data
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list' : latest_question_list,}
    return HttpResponse(template.render(context, request))

# Single question ka detail show karne ke liye method
def detial(request, question_id):
    return HttpResponse("You are looking at the question %s" % question_id)

# Question ke result ko show karnae ke liye method
def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)