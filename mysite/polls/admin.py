from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # ye simple question form me date pahle aur question_text ko bad me show karega.
    # fields = ['pub_date', 'question_text']

    # file set ka use karne section bana 
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

# choice ko show karne ke liye admin me register kiya
admin.site.register(Choice)
