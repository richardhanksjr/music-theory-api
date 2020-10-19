from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from questions.questions.simple_questions import SimpleIntervalIs
from questions.models import Question, Tag
from api.views import Answer, GetRandomQuestion

User = get_user_model()


class TestAnswer(TestCase):
    def setUp(self):
        pass
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="foo", email='test@test.com', password='foo')

    @classmethod
    def setUpTestData(cls):
        Question.objects.create(class_name="SimpleIntervalIs", module_name='simple_questions')
        cls.simple_interval = SimpleIntervalIs()
        cls.url = reverse("api:answer")

    def test_return_correct_json_keys(self):
        view = Answer.as_view()

        key = self.simple_interval.key
        answer = self.simple_interval.answer
        request = self.factory.post(self.url, {'key': key, 'answer': answer})
        # User must be set this way because of allauth
        request.user = self.user
        response = view(request)

        self.assertListEqual(['correct', 'correct_answer'], list(response.data.keys()))

    def test_400_on_bad_request(self):
        request = self.factory.post(self.url)
        request.user = self.user
        view = Answer.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 400)

class TestHelpSteps(TestCase):
    def setUp(self):
        self.test_question = Question.objects.create(class_name='SimpleIntervalIs', module_name='simple_questions')
        self.question = SimpleIntervalIs()
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')

    def test_help_steps(self):
        expected_steps = ({'prompt': 'What is a simple interval?',
                             'answer': 'an interval of one octave or less.'},)
        actual_steps = self.question.help_steps
        self.assertEqual(expected_steps, actual_steps)

    def test_help_steps_added_to_cache(self):
        cache_key = self.question.key
        steps_from_cache = cache.get(cache_key)
        self.assertEqual(steps_from_cache['help_steps'], self.question.help_steps)

    def test_help_steps_exist_at_correct_url(self):
        user = User.objects.create(email="testuser@email", password="testpass")
        self.client.force_login(self.user)
        url = reverse('api:help-steps')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'prompt')