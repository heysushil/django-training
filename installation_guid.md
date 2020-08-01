# Django installation guid

### मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

### कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

### और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

## For installing Django in your system you need following things before installing Django

1. Python(Try to install latest version)
2. Pip 
3. Then you will install Django by running this command - py -m pip install Django
4. Agter that you also need to have database. Best caase to use xampp server and use phpmyadmin which also provide user interface

## Setps to install Django and app

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
1. For using mysql neet to download mysqlclient for that [visti this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
1. in this tutorail with python version 3.8.2 using this = mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl
1. For connecting database with Django we need to have server name, database user name, dabase user password and database name

## Settings for Database:

1. first thing to change your time zone on parent folder mysite->settings.py => TIME_ZONE = 'Asia/Kolkata'
1. also creat static folder for storing css,js,image which you create in root folder mystie->static 
1. also in root folder -> settings.py at bottom befor static_url past this line => STATIC_ROOT = os.path.join(BASE_DIR, 'static')
1. root folder ->settings.py changes on databse
1. after provide all database details at final run => py manage.py migrate this command to create all required tables in your choosen database


## Command realted to model when you creat model in your app

> Note: Remeber you are using mysql database by Xampp server and for that you need to also start xampp server and in which you start apache and mysql.

1. first thing is to add your app name into settings.py installed_apps section. for know go to check settings.py installed_app section to know more.
1. then created 2 classes Question and Choice in models.py chick this file for more.
1. then need to migrate it for generating migrations file whcih sotes in your apps migration folder for more see migration folder in polls app. for that need to run this command -> py manage.py makemigrations polls
1. after that need to generate sql qury using migration file and for that need to run this command -> py manage.py sqlmigrate polls 0001 . in my case app name is polls and file name is 0001 which is auto generated
1. then finally for creating tables in our database need to run final command -> py manage.py migrate
1. know you have successfully get the tables of Qustion and Choice in your database. for that you need to refresh your database.

## Neet to add some data on Question and Choice table by shell:

1. For opeing shell in terminal run : py manage.py shell