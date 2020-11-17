from django.test import TestCase
from django.core.cache import cache
from questions.questions.intervals import SemitonesInInterval, IntervalRaisedLoweredIs, IntervalChangedByStepBecomesQuality, InvertedInterval



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

    def test_answer_is_correct(self):
        expected_answer = "Minor"
        self.assertEqual(expected_answer, self.question.answer)

        

class TestIntervalChangedByStepBecomesQuality(TestCase):

    def setUp(self):
        self.question = IntervalChangedByStepBecomesQuality('m', 'larger')

    def test_question(self):
        expected_question = "A minor interval made larger by a half step becomes what type of interval?"
        self.assertEqual(expected_question, self.question.question)

    def test_answer(self):
        expected_answer = "major"
        self.assertEqual(expected_answer, self.question.answer)


class TestCompoundIntervalRelationship(TestCase):

    def setUp(self):
        self.question = CompoundIntervalRelationship()

    def test_for_correct_question(self):
        expected_question = """ When compounded, the interval produced by combining the 3rd 
                                scale degree of an Eb whole tone scale with the mediant of 
                                an E major pentatonic scale bears what relation to the 
                                interval of a minor 9th """
        self.assertEqual(expected_question, self.question.question)

    def test_for_correct_answer(self):
        expected_answer = 'It is the same quality'
        self.assertEqual(expected_answer, self.question.answer)

