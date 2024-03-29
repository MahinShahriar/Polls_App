import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=10)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

