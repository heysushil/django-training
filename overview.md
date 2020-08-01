# Introduction of Django Framwork

### मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

### कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion


## Work behavior of Model
### projectname/news/models.py

    from django.db import models
> note: when we creat class in model then the name of class will be became table name in database
    class Reporter(models.Model):
        full_name = models.CharField(max_lenght=100)

        def __str__(self):
            retrun self.full_name

    class Article(models.Model):
        pub_date = models.DateField()
        headline = models.CharField(max_length=200)
        content = models.TextField()
        reporter = models.ForeingKey(Reporter, on_delete=models.CASCADE)

        def __str__(self):
            return self.headline

### After creating model need to call database

> Note: makemigrations use to check all available tables in database
    python manage.py makemigrations
> Note: migrate use to create table in databse if table not exists
    python mange.py migrate

## Already available Free API's in Django 

    from news.models import Article, Reporter
> for checking how many rows exists in reporter table
    Reporter.objects.all()
    <QuerySet []>

> inseter new reporer in our table
    r = Reporter(full_name='Virendra')
> after passing values to class need to save it
    r.save()

> want to check user id in repoter table
    r.id

> again check reporters in table
    Reporter.objects.all()
> provide list of all repoters in result

> for geting only reporter name from table
    r.full_name

> for geting names from repoter table also have lookup method naem get()
    Reporter.objects.get(id=1)

> useing fillter to find user by stating name Vir
    Reporter.objects.get(full_name_startswith='Vir')

> only get users who have nd in name
    Reporter.objects.get(full_name_contains='Vir')

> when tring to get non-existsing details
    Reporter.objects.get(id=2)
> DoesNotExists

> know creating new article
    from datetime import date
    a = Article(pub_date=date.today(), headlin='Django is great', contet='THis is great', reporter=r)
> rember when ever insert new entry on table must user save method to save this on table
    a.save()

    Article.objects.all()

> if we want to chekc which reporter written this artilce
    r = a.reporter
    r.full_name

> when want to get all articels of one reporter then use this
    r.article_set.all()

> by using filler get all article behalf of reporter
    Article.obejcts.filter(reporter_full_name_startswith='Vir')

> for updateing reporter name
    r.full_name = 'Virendra Kumar'
    r.save()

> at the last want to deleter the reporter object
    r.delete()


> for know we have our model name as models.py in path: mystie/news/models.py
> for admin we need to create admin.py in our news folder

    from django.contrib import admin
    from . import models

    admin.site.register(models.Article)

## Django URL Desing

> if you want to get url by sitename/year or month
> crete new file in mystie/news/urls.py

    from django.urls import path
    from . import views

    urlpatterns = [
        path('articles/<int:year>/', views.year_archive),
        path('articles/<int:year>/<int:month>/', views.month_archvie)
    ]
> assume you visittes website name news: url of news in case of articel and year
> www.news.com/articles/2020/

## Django View
> Note: we have new file in mystie/news/views.py
    from django.shortcuts import render
    from .models import Article

    def year_archive(request, year):
        a_list = Article.objects.fillter(pub_date__year=year)
        context = {'year': year, 'article_list': a_list}
        returnd render(request, 'news/year_archive.html', context)

## Templates desing

        Note: THis is basic sysntax of html
        <html>
            <head>
                <title>Django</title>
            </head>
            <body>
                <h1>Hello Django</h1>
            </body>
        </html>

Note: this html code is using django code to shwo articls

{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Article for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}


>Note: in uper html code at first we exteded base.html file which is static and for which we are createing base.html file sepratly and used it in multiple files as per requiremnts

>Note: mysite/templates/base.html

{% load static %}
<html>
<head>
    <title>{% block title %}{% endbloack %}</title>
</head>
<body>
    <img src="{% static "images/logo.png" %}" alt="hi">
    {% block content %}{% endblock %}
</body>
</html>