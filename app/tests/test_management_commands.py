from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.management import call_command

from questions.models import Question

User = get_user_model()

class TestDockerSynce(TestCase):

    def test_existing_questions_removed(self):
        # Create initial questions
        self.question = Question.objects.create(class_name='test', module_name="test")

        # Sanity check
        num_questions = Question.objects.all().count()
        self.assertEqual(1, num_questions)

        call_command('docker_sync')
        try:
            Question.objects.get(class_name=self.question.class_name,
                                 module_name=self.question.module_name)
            self.assertFalse(True)
        except Question.DoesNotExist:
            self.assertTrue(True)

    def test_two_users_created(self):
        call_command('docker_sync')
        num_users = User.objects.all().count()
        self.assertEqual(2, num_users)

    def test_regular_user_created(self):
        call_command('docker_sync')
        try:
            user = User.objects.get(email='regular@test.com')
            self.assertTrue(True)
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_superuser)
        except User.DoesNotExist:
            self.assertFalse(True)
        
    def test_admin_user_created(self):
        call_command('docker_sync')
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
        call_command('docker_sync')
        self.assertNotEqual(0, Question.objects.all().count())
