from django.test import TestCase
from questions.questions.major_scale_questions import SimpleScaleDegreeMajor
from django.core.cache import cache


class SimpleIntervalIsTest(TestCase):
    def setUp(self):
        self.question = SimpleScaleDegreeMajor(tonic='C', scale_degree_index=5)

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['answer'], self.question.answer)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
