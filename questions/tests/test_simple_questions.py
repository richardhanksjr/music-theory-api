from django.test import TestCase
from questions.questions.simple_questions import SimpleIntervalIs, InvertedQualityIs, TritoneIs, CouldBePerfectInterval
from django.core.cache import cache
from questions.models import Question, Tag


class SimpleIntervalIsTest(TestCase):
    def setUp(self):
        self.question_model = Question.objects.create(class_name='SimpleIntervalIs', module_name='simple_questions')
        tag = Tag.objects.create(name="A Tag")
        tag.question.add(self.question_model)
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


    def test_returns_correct_tags(self):
        self.assertListEqual(['A Tag'], list(self.question.tags))

    def test_correct_weight(self):
        self.assertEqual(1, self.question.weight)


class InvertedQualityIsTest(TestCase):

    def test_same_perfect_true(self):
        question = InvertedQualityIs(interval_quality='perfect', same=True)
        self.assertEquals("True", question.answer)

    def test_not_same_perfect_false(self):
        question = InvertedQualityIs(interval_quality='perfect', same=False)
        self.assertEquals("False", question.answer)

    def test_same_major_false(self):
        question = InvertedQualityIs(interval_quality='major', same=True)
        self.assertEquals("False", question.answer)

    def test_not_same_major_true(self):
        question = InvertedQualityIs(interval_quality='major', same=False)
        self.assertEquals("True", question.answer)

    def test_same_minor_false(self):
        question = InvertedQualityIs(interval_quality='minor', same=True)
        self.assertEquals("False", question.answer)

    def test_not_same_minor_true(self):
        question = InvertedQualityIs(interval_quality='minor', same=False)
        self.assertEquals("True", question.answer)

    def test_same_diminished_false(self):
        question = InvertedQualityIs(interval_quality='diminished', same=True)
        self.assertEquals("False", question.answer)

    def test_not_same_diminished_true(self):
        question = InvertedQualityIs(interval_quality='diminished', same=False)
        self.assertEquals("True", question.answer)

    def test_same_augmented_false(self):
        question = InvertedQualityIs(interval_quality='augmented', same=True)
        self.assertEquals("False", question.answer)

    def test_not_same_augmented_true(self):
        question = InvertedQualityIs(interval_quality='augmented', same=False)
        self.assertEquals("True", question.answer)


class TritoneIsTest(TestCase):

    def setUp(self):
        self.question = TritoneIs()

    def test_question(self):
        expected_question = "A TRITONE is:"
        self.assertEqual(expected_question, self.question.question)

    def test_answer(self):
        expected_answer = "An augmented 4th"
        self.assertEqual(expected_answer, self.question.answer)


class CouldBePerfectIntervalTest(TestCase):

    def setUp(self):
        self.question = CouldBePerfectInterval()

    def test_question(self):
        expected_question = "All of the following could be perfect intervals except:"
        self.assertEqual(expected_question, self.question.question)

    def test_answer(self):
        expected_answer = "Third"
        self.assertEqual(expected_answer, self.question.answer)