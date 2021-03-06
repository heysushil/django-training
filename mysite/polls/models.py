from django.utils import timezone
import datetime
from django.db import models

# Create your models here.

# create a Question class which store question and date
# models.Model is parent class whcih inherits by child class Question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # define str method to return string
    def __str__(self):
        return self.question_text

    # mehtod to get recent question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# also creating a choice class which have question related choices 
'''
MySQL:
1. databse have tables
2. tables have number fildes
3. in database have concept of kyes which is likely:
    primary key
    foreing key
    candidate key
    unique key
    super key


Example Tables:

table 1: user table (store user detials only and have unique id => primary key)
table 2: expense table (store all expnecse and have 1 unique id => primary key also expense table have user id for connecting user table with expense table)
'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # creat str method to get all choice
    def __str__(self):
        return self.choice_text

