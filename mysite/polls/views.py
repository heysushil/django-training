from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
# import django.template.loader as loader
from django.template import loader
# improt djangos generic modul to use it
from django.views import generic

from .models import Question, Choice
# Create your views here.

# MVC
# MVT

'''
Genric or predefine child class use ke liye setups:

1. Convert url to use generic code?
2. Hamare userdefine methods ko replace karenge classes se is case me main pahle ke methods ko comment kar raha hu taki check karte time uska bhi kar sako.
3. Use generic methos 
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Return 5 latest question by this.
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # agar user choice ko select kar rah hai ya nahi usko handel karna hai $_POST['choice'] | $this->input->post('choice')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Replay abotu choice not selected
        return render(request, 'polls/detail.html', {'questiondata':question, 'error_message': 'You didn\'t select any choice.',})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# -------------------------------------------------------
#        Hamare purane methods jo ab nahi rahe
# -------------------------------------------------------

# # index is a default function
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # define a html page in whcih you want to share the data
#     context = {'latest_question_list' : latest_question_list,}
#     return render(request, 'polls/index.html', context)

# # Single question ka detail show karne ke liye method
# def detial(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exists.')
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'questiondata' : question})

# # Question ke result ko show karnae ke liye method
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # response = "You are looking at the result of question %s."
#     # return HttpResponse(response % question_id)
#     data = {'question': question}
#     return render(request, 'polls/results.html', data)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # agar user choice ko select kar rah hai ya nahi usko handel karna hai $_POST['choice'] | $this->input->post('choice')
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Replay abotu choice not selected
#         return render(request, 'polls/detail.html', {'questiondata':question, 'error_message': 'You didn\'t select any choice.',})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# -------------------------------------------------------
#  End section of Hamare purane methods jo ab nahi rahe
# -------------------------------------------------------