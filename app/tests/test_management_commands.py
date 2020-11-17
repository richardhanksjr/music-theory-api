import sys
from unittest import mock
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.management import call_command
from app.management.commands.docker_sync import Command
from questions.questions import _questions_data

from questions.models import Question

User = get_user_model()

class TestDockerSync(TestCase):

    def setUp(self):
        self.question_class = mock.MagicMock()
        self.question_class.__name__ = 'TestQuestionClass'
        self.question_class.__module__ = 'questions.questions.question_module'

    def test_existing_questions_removed(self):

        # Sanity check
        num_questions = Question.objects.all().count()
        self.assertEqual(0, num_questions)

        # Mock _questions_data import
        Command._process(questions=[self.question_class], tags=[])
        try:
            Question.objects.get(class_name=self.question_class.__name__,
                                 module_name=self.question_class.__module__)
            self.assertTrue(True)
        except Question.DoesNotExist:
            self.assertFalse(True)

    def test_two_users_created(self):
        Command._process(questions=[self.question_class], tags=[])
        num_users = User.objects.all().count()
        self.assertEqual(2, num_users)

    def test_regular_user_created(self):
        Command._process(questions=[self.question_class], tags=[])
        try:
            user = User.objects.get(email='regular@test.com')
            self.assertTrue(True)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
        except User.DoesNotExist:
            self.assertFalse(True)
        
    def test_admin_user_created(self):
        Command._process(questions=[self.question_class], tags=[])
        try:
            user = User.objects.get(email='admin@test.com')
            self.assertTrue(True)
            self.assertTrue(user.is_staff)
            self.assertTrue(user.is_superuser)
        except User.DoesNotExist:
            self.assertFalse(True)

    def test_questions_match_fixtures(self):
        # Sanity test
        self.assertEqual(0, Question.objects.all().count())
        Command._process(questions=[self.question_class], tags=[])
        self.assertNotEqual(0, Question.objects.all().count())
