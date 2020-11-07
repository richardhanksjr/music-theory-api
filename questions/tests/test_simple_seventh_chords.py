from django.test import TestCase
from questions.questions.simple_seventh_chord_question import SimpleMajorSeventh
from django.core.cache import cache
from questions.models import Question
from questions.questions._utilities import random_major_seventh_chord

class SimpleMajorSeventhTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleMajorSeventh')
        self.question = SimpleMajorSeventh(chord=random_major_seventh_chord(), chord_quality='major seventh chord')

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)