from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# question se realtaed choice show karne ke liye
'''
Question form me choices fields show karne ke liye:

1. admin.StackedInline: is ke use se choices fields individual show hoti hain. Jisme ki kafi lines use ho jatei hain. Ya fir ye individual choice section me fields show karta hai.

2. admin.TabularInline: Ye choices ko table form me show karta hai. Is ke use se form chota aur compac ho jata hai.
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    # ye extra 3 qeustion form par 3 blank fiedls dega jisme ki aap choice likh sakte ho.
    extra = 3

# Question form par date aur text ak section show karene ke liye.
class QuestionAdmin(admin.ModelAdmin):
    # ye simple question form me date pahle aur question_text ko bad me show karega.
    # fields = ['pub_date', 'question_text']

    # file set ka use karne section bana 
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # yeha par choices ko fields ko add karna hai
    inlines = [ChoiceInline]
    
    '''
    list_display: ye admin me quesiton list ko show karega aur us list me hum jo show karana cahte hain. 
    Usko hum yaha se tuple ke form me pass karenge.
    ''' 
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # list_filter ka use karna hai search box show karne ke liye
    list_filter = ['pub_date']
    

admin.site.register(Question, QuestionAdmin)

# choice ko show karne ke liye admin me register kiya
admin.site.register(Choice)
