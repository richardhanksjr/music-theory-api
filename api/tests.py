from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from questions.questions.simple_questions import SimpleIntervalIs

User = get_user_model()


class TestAnswer(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.simple_interval = SimpleIntervalIs()
        cls.client = APIClient()
        user = User.objects.create_user(username="foo")
        cls.client.force_login(user)

    def test_return_correct_json_keys(self):
        key = self.simple_interval.key
        answer = self.simple_interval.answer
        url = reverse('answer')
        response = self.client.post(url, {'key': key, 'answer': answer}).data
        self.assertListEqual(['correct', 'correct_answer'], list(response.keys()))

    def test_400_on_bad_request(self):
        url = reverse('answer')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)