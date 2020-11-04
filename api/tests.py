from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from questions.questions.simple_questions import SimpleIntervalIs
from questions.models import Question, Tag, Attempt
from api.views import Answer, GetRandomQuestion, HelpSteps, LogAttempt

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
        self.factory = APIRequestFactory()
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

    def test_return_correct_json_key(self):
        self.url = reverse('api:help-steps')
        key = self.question.key
        request = self.factory.post(self.url, {'key': key})

    def test_405_if_get_request(self):
        self.url = reverse('api:help-steps')
        request = self.factory.get(self.url)
        request.user = self.user
        view = HelpSteps.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 405)

    def test_keys_match(self):
        question_key = self.question.key
        cached_response = cache.get(question_key)
        self.assertEqual(question_key, cached_response['key'])


class TestAttempt(TestCase):

    def setUp(self):
        self.test_question = Question.objects.create(class_name='SimpleIntervalIs', module_name='simple_questions')
        self.question = SimpleIntervalIs()
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')
        # self.test_attempt = Attempt.objects.create(
        #                         class_name='SimpleIntervalIs', 
        #                         module_name='simple_questions',
        #                         correct=True)

    def test_class_name_added_to_cache(self):
        cache_key = self.question.key
        cache_items = cache.get(cache_key)
        self.assertEqual(cache_items['class_name'], self.question.class_name)
        self.assertEqual(cache_items['answer'], self.question.answer)

    def test_attempt_is_created(self):
    
        self.attempts = Attempt.objects.all()
        # self.assertEqual(self.attempts, 0)


        cache_key = self.question.key
        cache_items = cache.get(cache_key)

        print(self.attempts)
     


    def test_return_correct_json_keys(self):
        
        view = LogAttempt.as_view()
        self.url = reverse('api:attempt')
        class_name = self.question.class_name
        user = self.user

        self.factory = APIRequestFactory()
        request = self.factory.post(self.url, {'class_name': class_name, 'user': user})
        request.user = self.user
        response = view(request)
        