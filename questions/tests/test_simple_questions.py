from django.test import TestCase
from questions.questions.simple_questions import SimpleIntervalIs


class SimpleIntervalIsTest(TestCase):
    def setUp(self):
        self.question = SimpleIntervalIs()

    def test_question_params(self):
        expected_params = {'question_type': "simple-interval-is"}
        actual_params = self.question.question_params
        self.assertDictEqual(expected_params, actual_params)