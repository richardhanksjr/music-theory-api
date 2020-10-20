from django.test import TestCase
from questions.questions.minor_scale_questions import SimpleScaleDegreeMinor
from django.core.cache import cache
from questions.models import Question


class SimpleScaleDegreeMinorTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleScaleDegreeMinor')
        self.question = SimpleScaleDegreeMinor(tonic='C', scale_degree_index=5)

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)

    def test_correct_question(self):
        expected_question = "What is the sixth scale degree of C natural Minor?"
        self.assertEqual(self.question.question, expected_question)

    def test_correct_answer(self):
        # Ab using unicode for flat sign u266D
        self.assertEqual(u'A\u266D', self.question.answer)
