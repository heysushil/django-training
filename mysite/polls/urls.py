from django.urls import path
from . import views

# in app urls.py file we will creat a path which we will pass to our main project urls file
urlpatterns = [
    # in path have 4 arguemts
    # 1. route: 127.0.0.1/8000/polls/
    # 2. view: in this pass a method name of views
    # 3. kwargs: 
    # 4. name: 
    path('', views.index, name='index'),
    # path('user/', views.user, name='user'),
]
