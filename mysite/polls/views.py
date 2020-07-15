from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# index is a default function
def index(request):
    return HttpResponse('Hello Django Freamwork')

# def user(request):
#     return HttpResponse('Hello new user')


# xampp server