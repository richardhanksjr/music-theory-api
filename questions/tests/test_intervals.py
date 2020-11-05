from django.test import TestCase
from django.core.cache import cache
from questions.questions.intervals import SemitonesInInterval, IntervalRaisedLoweredIs, InvertedInterval


class TestSemitonesInInterval(TestCase):

    def setUp(self):
        self.question = SemitonesInInterval(interval_quality='P', interval_number=5)

    def test_for_correct_question(self):
        expected_question = "How many semitones are there in a/an Perfect Fifth?"
        self.assertEqual(expected_question, self.question.question)

    def test_for_correct_answer(self):
        expected_answer = 7
        self.assertEqual(expected_answer, self.question.answer)


class TestIntervalRaisedLoweredIs(TestCase):

    def setUp(self):
        self.question = IntervalRaisedLoweredIs(lower_pitch='C2', upper_pitch="G2", lower_direction='lowered',
                                                upper_direction='raised', lower_pitch_num_octaves=1,
                                                upper_pitch_num_octaves=1)

    def test_for_correct_answer(self):
        expected_answer = "P19"
        self.assertEqual(expected_answer, self.question.answer)

    def test_for_correct_question(self):
        expected_question = "The interval C2 to G2 becomes which interval when C2 is lowered 1 " \
                            "octave(s) and G2 is raised 1 octave(s)?"
        self.assertEqual(expected_question, self.question.question)


class TestInvertedInterval(TestCase):

     def setUp(self):
         self.question = InvertedInterval(interval_quality='Major')

     def test_question(self):
         expected_question = "When inverted, a Major interval becomes:"
         self.assertEqual(expected_question, self.question.question)

     def test_question_added_to_cache(self):
         cache_key = self.question.key
         question_from_cache = cache.get(cache_key)
         self.assertEqual(question_from_cache['answer'], self.question.answer)
         self.assertEqual(question_from_cache['question'], self.question.question)
         self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)

     def test_answer_is_correct(self):
         expected_answer = "Minor"
         self.assertEqual(expected_answer, self.question.answer)
