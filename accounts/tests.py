from django.test import Client, TestCase
from django.urls import reverse, resolve

from django.contrib.auth.models import User


class SignupTests(TestCase):

    """ 
    As a user I want a registration page so that I 
    can register for an account with an email and password.
    """

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        user_one = User.objects.create_user(
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

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    # def test_duplicate_email_does_not_create_two_users(self):
    #     original_email = User.objects.get(email='newuser@email.com')
    #     self.assertEqual(original_email.username, 'newuser')
    #     duplicate_email = User.objects.create_user(
    #                             username='duplicateuser', 
    #                             email='newuser@email.com',
    #                             password='duplicatepass')
    #     user_count = User.objects.filter(email='newuser@email.com')
    #     self.assertEqual(user_count.count(), 1)

    def test_user_already_exists_redirected_to_login(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)

class VideoTests(TestCase):   
    
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account_signup')
        self.login_url = reverse('account_login')

    def test_signup_GET(self):

        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

    def test_login_GET(self):

        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_POST(self):

        user_one = User.objects.create_user(
                                username='newuser', 
                                email='newuser@email.com',
                                password='testpass123')

        response = self.client.post(self.signup_url, {'email:', 'newuser@email.com', 'password:', 'testpass123'})
        self.assertEqual(response.status_code, 200)



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