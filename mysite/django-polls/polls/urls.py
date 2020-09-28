# from mysite.polls.views import results
from django.urls import path
from . import views

# in app urls.py file we will creat a path which we will pass to our main project urls file

# discribe app name to which these all urls are realted
app_name = 'polls'
urlpatterns = [
    # in path have 4 arguemts
    # 1. route: 127.0.0.1/8000/polls/
    # 2. view: in this pass a method name of views
    # 3. kwargs: 
    # 4. name: 
    # index url is: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/1/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
