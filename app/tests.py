from django.test import TestCase

from django.test import Client

class TestTest(TestCase):
    def test_tests_works(self):
        self.assertTrue(True)


class QuestionsTest(TestCase):
    def test_questions_page_exists(self):
        self.client = Client()
        response = self.client.get("/questions/")
        self.assertEqual(response.status_code, 200)

