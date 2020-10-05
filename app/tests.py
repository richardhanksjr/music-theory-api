from django.test import TestCase, SimpleTestCase, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse

from .views import LandingPageView, IndexPageView


class TestTest(TestCase):
    def test_tests_works(self):
        self.assertTrue(True)


# class LandingPageTests(SimpleTestCase):
    def setUp(self):
        self.url = reverse('app:landing')
        self.response = self.client.get(self.url)

    def test_landing_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_landing_page_template(self):
        self.assertTemplateUsed(self.response, 'app/landing.html')

    def test_landing_page_contains_correct_html(self):
        self.assertContains(self.response, 'Music Theory Dojo')

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