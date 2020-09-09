import datetime

from django.test import TestCase
from django.utils import timezone

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
