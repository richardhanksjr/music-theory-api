from django.test import Client, TestCase
from django.urls import reverse, resolve

from django.contrib.auth.models import User

Create your tests here.

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

class LoginTests(TestCase):

    """ 
    As a user I would link a user model where email is the username so that I can 
    log into the app using my email
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                                username='newuser', 
                                email='newuser@email.com',
                                password='testpass123')
        user_two = User.objects.create_user(
                                username='usertwo', 
                                email='usertwo@email.com',
                                password='testpass222')
        user_three = User.objects.create_user(
                                username='userthree', 
                                email='userthree@email.com',
                                password='testpass333')

    def test_login_returns_status_code_200(self):
        url = reverse('account_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_using_email_as_id(self):
        c = Client()
        login = c.login(email='newuser@email.com', password='testpass123')
        self.assertEqual(login, True)