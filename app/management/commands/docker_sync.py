from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from allauth.account.admin import EmailAddress

from questions.models import Question, Tag
from questions.questions._questions_data import questions, tags


User = get_user_model()

class Command(BaseCommand):
    """
    manage.py command used in local development only.  Used for syncing development 
    databases within Docker using 
    """
    @staticmethod
    def _process(questions=questions, tags=tags):
        Question.objects.all().delete()
        # call_command('loaddata', 'questions.json', verbosity=0)
        # Clear the database to start clean
        Question.objects.all().delete()
        Tag.objects.all().delete()

        # Load questions into database
        for question in questions:
            Question.objects.create(class_name=question.__name__, module_name=question.__module__)

        # Load tags
        for tag in tags:
            _tag = Tag.objects.create(name=tag["name"])
            _tag.question.add(*[Question.objects.get(class_name=question.__name__, module_name=question.__module__) for question in tag['questions']])
            _tag.save()

        # Create regular user
        regular = User.objects.create_user(email='regular@test.com', username='regular', password='test123')
        # Create admin user
        admin = User.objects.create_superuser(email='admin@test.com', username='admin', password='test123')
        EmailAddress.objects.create(user=regular, email=regular.email, primary=True, verified=True)
        
        EmailAddress.objects.create(user=admin, email=admin.email, primary=True, verified=True)

    def handle(self, *args, **kwargs):
        self._process()

