from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from allauth.account.admin import EmailAddress

from questions.models import Question


User = get_user_model()

class Command(BaseCommand):
    """
    manage.py command used in local development only.  Used for syncing development 
    databases within Docker using 
    """

    def handle(self, *args, **kwargs):
        Question.objects.all().delete()
        call_command('loaddata', 'questions.json', verbosity=0)
        # Create regular user
        regular = User.objects.create_user(email='regular@test.com', username='regular', password='test123')
        # Create admin user
        admin = User.objects.create_superuser(email='admin@test.com', username='admin', password='test123')
        EmailAddress.objects.create(user=regular, email=regular.email, primary=True, verified=True)
        
        EmailAddress.objects.create(user=admin, email=admin.email, primary=True, verified=True)

