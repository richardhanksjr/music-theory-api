from django.test import TestCase
from questions.questions.intervals import SemitonesInInterval


class TestSemitonesInInterval(TestCase):

    def setUp(self):
        self.question = SemitonesInInterval(interval_quality='P', interval_number=5)

    def test_for_correct_question(self):
        expected_question = "How many semitones are there in a/an Perfect Fifth?"
        self.assertEqual(expected_question, self.question.question)

    def test_for_correct_answer(self):
        expected_answer = 7
        self.assertEqual(expected_answer, self.question.answer)
