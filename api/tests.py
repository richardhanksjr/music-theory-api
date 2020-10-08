from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from questions.questions.simple_questions import SimpleIntervalIs
from questions.models import Question
from api.views import Answer, GetRandomQuestion

User = get_user_model()


class TestAnswer(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        # self.user = User.objects.create_user(username="foo", email='test@test.com', password='foo')

    # @classmethod
    # def setUpTestData(cls):
    #     Question.objects.create(class_name="SimpleIntervalIs", module_name='simple_questions')
    #     cls.simple_interval = SimpleIntervalIs()
    #     cls.url = reverse("answer")

    # def test_return_correct_json_keys(self):
    #     view = Answer.as_view()
    #
    #     key = self.simple_interval.key
    #     answer = self.simple_interval.answer
    #     request = self.factory.post(self.url, {'key': key, 'answer': answer})
    #     # User must be set this way because of allauth
    #     request.user = self.user
    #     response = view(request)
    #
    #     self.assertListEqual(['correct', 'correct_answer'], list(response.data.keys()))
    #
    # def test_400_on_bad_request(self):
    #     request = self.factory.post(self.url)
    #     request.user = self.user
    #     view = Answer.as_view()
    #     response = view(request)
    #     self.assertEqual(response.status_code, 400)
