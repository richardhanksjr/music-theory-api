from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class SignupTests(TestCase):

    """ 
    As a user I want a registration page so that I 
    can register for an account with an email and password.
    """
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

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)

class LoginTests(TestCase):

    """ 
    As a user I would link a user model where email is the username so that I can 
    log into the app using my email
    """

    def setUp(self):
        url = reverse('account_login')
        self.response = self.client.get(url)
        self.client = Client()
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')

    def test_login_using_email_as_id(self):
        c = Client()
        login = c.login(email='newuser@email.com', password='testpass123')
        self.assertEqual(login, True)

    def test_login_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/login.html')
        self.assertContains(self.response, 'Log In')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

class LogoutTests(TestCase):

    """
    As a logged-in user I would like a logout link so that I can
    log out of my account
    """

    def setUp(self):
        url = reverse('account_logout')
        self.response = self.client.get(url)
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')
        
    
    def test_user_not_logged_in_redirected_to_landing_page(self):
        url = reverse('account_logout')
        self.response = self.client.get(url, follow=True)
        self.assertTemplateUsed(self.response, 'app/landing.html')

    def test_logout_page_template_used(self):
        self.client.force_login(self.user)
        url = reverse('account_logout')
        self.response = self.client.get(url)
        self.assertTemplateUsed(self.response, 'account/logout.html')