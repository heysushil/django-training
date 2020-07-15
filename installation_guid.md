# Django installation guid

## For installing Django in your system you need following things before installing Django

1. Python(Try to install latest version)
2. Pip 
3. Then you will install Django by running this command - py -m pip install Django
4. Agter that you also need to have database. Best caase to use xampp server and use phpmyadmin which also provide user interface

## Setps

1. first to use this command to install django:
    py -m pip install Django

1. Then need to create your project for that run this command:
    django-admin startproject projectname
1. for running django project run this command:
    py manage.py runserver
1. for creating new app in project you must have to in your project main file then run this command:
    py manage.py startapp polls

## Understanding of app in Django freamwork

1. each app is also a project

## Detail of root directory

1. mystie its a root directory
1. manage.py: 
1. mysite: inner folder
1. __init__.py: 
1. asgi.py: 
1. settings.py:
1. wsgi.py: 

## Polls app file directory:

1. __init__.py: defail and blank
1. admin.py: which use to connect with admin pannel
1. apps.py: which is for polls app
1. models.py: it's polls app model file
1. tests.py: use to creeate test cases
1. urls.py: it's manully create for creating url pattern
1. views.py: it's python code file

## Django using Database: Xampp and phpMyAdmin

1. By click in to insatll xampp server > [insall xampp server](https://www.apachefriends.org/xampp-files/7.4.8/xampp-windows-x64-7.4.8-0-VC15-installer.exe)
1. connect with xampp and Django fremawork
1. For connecting database with Django we need to have server name, database user name, dabase user password and database name