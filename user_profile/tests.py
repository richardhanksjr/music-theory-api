from django.test import TestCase, Client
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileTests(TestCase):

    def test_user_profile_is_created_when_user_is_created(self):
        self.assertTrue(UserProfile.objects.count() == 0)
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')
        self.assertTrue(UserProfile.objects.count() == 1)