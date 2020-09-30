from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import LandingPageView, IndexPageView


class TestTest(TestCase):
    def test_tests_works(self):
        self.assertTrue(True)

class LandingPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('app:landing')
        self.response = self.client.get(url)

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
        view = resolve('/landing/')
        self.assertEqual(
            view.func.__name__,
            LandingPageView.as_view().__name__
        )

class IndexPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('app:index')
        self.response = self.client.get(url)

    def test_index_page_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_index_page_url_resolves_indexpageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            IndexPageView.as_view().__name__
        )