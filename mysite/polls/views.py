from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
# import django.template.loader as loader
from django.template import loader 
from .models import Question
# Create your views here.

# index is a default function
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # define a html page in whcih you want to share the data
    context = {'latest_question_list' : latest_question_list,}
    return render(request, 'polls/index.html', context)

# Single question ka detail show karne ke liye method
def detial(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exists.')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'questiondata' : question})

# Question ke result ko show karnae ke liye method
def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)