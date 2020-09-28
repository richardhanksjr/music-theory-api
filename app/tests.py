from django.test import TestCase

from django.test import Client

class TestTest(TestCase):
    def test_tests_works(self):
        self.assertTrue(True)


class QuestionsTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_questions_page_exists_and_correct_template_used(self):
        response = self.client.get("/questions/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/questions.html')

    def test_question_exists_on_questions_page(self):
        response = self.client.get("/questions/")
        self.assertContains(response, 'name="question"')

    def test_questions_page_contains_four_multiple_choice_answers(self):
        response = self.client.get("/questions/")
        self.assertContains(response, '<form')
        self.assertContains(response, 'type="radio"', 4)

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')


