import datetime
from django.http import response

from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

# Create karna hai futrue question ko handle karne ke liye class
class QuestionModelTests(TestCase):
    # Yaha par ek method banate hain futere question ko handle karne ke lkye
    def test_was_published_recently_with_future_question(self):
        # time abhi se 30 day aage ko store kiya hai taki iska use kar ke future question ko jan sake.
        time = timezone.now() + datetime.timedelta(days=30)

        # ye humne future question table mese get karne ke liye kiya hai
        future_question = Question(pub_date=time)

        # yaha par humne future_qustion name ka object create kiya aur then TestCase ke method asserIs ka use kar ke 2 agruments pass kiya, 1: method ko call kiya, 2: value jo method ko run karne par dikhana hai wo.
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        # ye past question ko chek karne ke liye hai
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        # ye recnet question test case hai
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# new question create check ke liye method
def create_question(question_text, days):
    # Jo bhi qeustion create kiya gaya hai uski date agar past me hain to negative ya fir abhi publish hona hai to positive milega.
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    # agar koi question na ho to page par message show karan hai
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        # sabse pahle status check kiya
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # agar past question list milta hai to
    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # futre question hame index page par nahi dikha hai.
    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # incase agar future aur past dono question aate hain to kewal past question show karan hai.
    def test_future_question_and_past_question(self):
        create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    # agar 2 past question mil rahe hain to
    def test_two_past_question(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

# class for DetailView test cases
class QuestionDetailViewTests(TestCase):
    # future question detail ko roken ke liye test case
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # past question ke liye
    def test_past_question(self):
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse('polls:detail', args=(past_question.id))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

