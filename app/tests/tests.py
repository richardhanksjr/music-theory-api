from django.test import TestCase, SimpleTestCase, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse


from django.test.client import Client
from django.test.utils import override_settings
from allauth.utils import get_user_model
from allauth.account.decorators import verified_email_required



from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)

from app.views import LandingPageView, IndexPageView, ProfilePageView


from django.test import Client

class TestTest(TestCase):
    def test_tests_works(self):
        self.assertTrue(True)


class LandingPageTests(TestCase):
    def setUp(self):
        self.url = reverse('app:landing')
        self.response = self.client.get(self.url)

    def test_landing_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_landing_page_template(self):
        self.assertTemplateUsed(self.response, 'app/landing.html')

    def test_landing_page_contains_correct_html(self):
        self.assertContains(self.response, 'TheoryDojo')

    def test_landing_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_landing_page_url_resolves_landingpageview(self):
        view = resolve(self.url)
        self.assertEqual(
            view.func.__name__,
            LandingPageView.as_view().__name__
        )


class IndexPageTests(TestCase):
    factory = RequestFactory()

    def setUp(self):
        url = reverse('app:index')
        self.response = self.client.get(url)
        self.user = User.objects.create_user(username='joe', email='joe@test.com', password='qwerty')

    def test_index_page_url_resolves_indexpageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            IndexPageView.as_view().__name__
        )

    def test_login_required_on_IndexPageView(self):

        view = IndexPageView.as_view()

        # When user is not logged in, redirected to landing page
        request = self.factory.get(reverse('app:index'))
        request.user = AnonymousUser()
        response = view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual('/landing/?next=/', response.url)

        # When user is logged in, receive a status code of 200
        request = self.factory.get(reverse('app:index'))
        request.user = self.user
        response = view(request)
        self.assertEqual(response.status_code, 200)

class ProfilePageTests(TestCase):
    client = Client()
    factory = RequestFactory()

    def setUp(self):
        url = reverse('app:profile')
        self.response = self.client.get(url)
        self.user = User.objects.create_user(username='joe', email='joe@test.com', password='qwerty')

    def test_profile_page_url_resolves_profilepageview(self):
        view = resolve(reverse('app:profile'))
        self.assertEqual(
            view.func.__name__,
            ProfilePageView.as_view().__name__
        )

    def test_login_required_on_ProfilePageView(self):

        view = ProfilePageView.as_view()

        # When user is not logged in, redirected to landing page
        request = self.factory.get(reverse('app:profile'))
        request.user = AnonymousUser()
        response = view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual('/landing/?next=/profile/', response.url)

        # When user is logged in, receive a status code of 200
        request = self.factory.get(reverse('app:profile'))
        request.user = self.user
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

class NavBarTests(TestCase):
    """
    https://github.com/pennersr/django-allauth/blob/master/allauth/account/tests.py

    """

    def setUp(self):
        url = reverse('account_logout')
        self.response = self.client.get(url)
        self.user = User.objects.create_user(
                                username='newuser',
                                email='newuser@email.com',
                                password='testpass123')


    def _create_user(self, username="john", password="doe"):
        user = get_user_model().objects.create(username=username, is_active=True)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user


    def _create_user_and_login(self, usable_password=True):
        password = "doe" if usable_password else False
        user = self._create_user(password=password)
        self.client.force_login(user)
        return user

    def _logout_view(self, method):
        user = get_user_model().objects.create(username="john", is_active=True)
        user.set_password("doe")
        user.save()
        c = Client()
        c.login(username="john", password="doe")
        return c, getattr(c, method)(reverse("account_logout"))

    @override_settings(ACCOUNT_LOGOUT_ON_GET=True)
    def test_logout_view_on_get(self):
        c, resp = self._logout_view("get")
        self.assertTemplateUsed(resp, "account/messages/logged_out.txt")

    def test_login_redirects_to_index_route_when_authenticated(self):
        self._create_user_and_login()
        c = self.client
        response = c.get(reverse("account_login"))
        self.assertRedirects(response, "/", fetch_redirect_response=False)


    def test_random_question_link_uses_correct_template(self):
        user = User.objects.create(email="testuser@email", password="testpass")
        self.client.force_login(self.user)
        url = reverse('app:index')
        self.response = self.client.get(url)
        self.assertTemplateUsed(self.response, 'app/questions.html')

    def test_user_not_logged_in_cannot_access_random_question(self):
        url = reverse('app:index')
        self.response = self.client.get(url)
        self.assertRedirects(self.response, '/landing/?next=/')


    def test_homepage_does_not_contain_incorrect_html(self):
        url = reverse('app:index')
        self._create_user_and_login()
        response = self.client.get(url)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_profile_link_uses_correct_template(self):
        self.user = User.objects.create(email="testuser@email", password="testpass")
        self.client.force_login(self.user)
        profile_url = reverse('app:profile')
        self.response = self.client.get(profile_url)
        self.assertTemplateUsed(self.response, 'app/profile.html')

    def test_user_not_logged_in_cannot_access_profile(self):
        profile_url = reverse('app:profile')
        self.response = self.client.get(profile_url)
        self.assertRedirects(self.response, '/landing/?next=/profile/')

class EmailTests(TestCase):

    def test_email_verification_set_to_mandatory(self):
        user = get_user_model().objects.create(username="mike")
        email = EmailAddress.objects.create(
            user=user,
            email="mike@example.",
        )
        c = Client()
        # Signup
        c.get(reverse("account_login"))
        response = c.post(
            reverse("account_signup"),
            {
                "username": user,
                "email": email,
                "password1": "mikey",
            },
            follow=True
        )

        self.assertContains(response, 'ACCOUNT_EMAIL_VERIFICATION')
        self.assertContains(response, 'mandatory')
        self.assertContains(response, 'ACCOUNT_EMAIL_REQUIRED')
        self.assertContains(response, 'True')