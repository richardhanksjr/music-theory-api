from django.test import TestCase
from questions.questions.simple_triad_questions import SimpleMajorTriad, SimpleMinorTriad, SimpleDiminishedTriad, SimpleAugmentedTriad
from django.core.cache import cache
from questions.models import Question
from questions.questions._utilities import random_root_position_major_triad, random_root_position_minor_triad, random_root_position_diminished_triad, random_root_position_augmented_triad


class SimpleMajorTriadTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleMajorTriad')
        self.question = SimpleMajorTriad(triad=random_root_position_major_triad(), chord_degree='third')

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)

class SimpleMinorTriadTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleMinorTriad')
        self.question = SimpleMajorTriad(triad=random_root_position_minor_triad(), chord_degree='third')

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)

class SimpleDiminishedTriadTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleDiminishedTriad')
        self.question = SimpleMajorTriad(triad=random_root_position_diminished_triad(), chord_degree='third')

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)

class SimpleAugmentedTriadTest(TestCase):
    def setUp(self):
        Question.objects.create(class_name='SimpleAugmentedTriad')
        self.question = SimpleMajorTriad(triad=random_root_position_augmented_triad(), chord_degree='third')

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(3, self.question.weight)