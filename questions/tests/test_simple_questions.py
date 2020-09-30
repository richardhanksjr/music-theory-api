from django.test import TestCase
from questions.questions.simple_questions import SimpleIntervalIs
from django.core.cache import cache


class SimpleIntervalIsTest(TestCase):
    def setUp(self):
        self.question = SimpleIntervalIs()

    def test_question_params(self):
        expected_params = {'question_type': "simple-interval-is"}
        actual_params = self.question.question_params
        self.assertDictEqual(expected_params, actual_params)

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['answer'], self.question.answer)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
