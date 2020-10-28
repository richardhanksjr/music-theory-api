import random
from music21 import interval
from questions.questions.questions import Question
from ._utilities import random_numbers_answer_options



class SemitonesInInterval(Question):
    interval_qualities = ['a', 'd', 'm', 'M', 'p']
    interval_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def __init__(self, interval_quality=None, interval_number=None):
        self.interval_quality = interval_quality if interval_quality else random.choice(self.interval_qualities)
        self.interval_number = interval_number if interval_number else random.choice(self.interval_numbers)
        self._generate_interval()
        super().__init__()

    def _generate_interval(self):
        self._interval = None
        while self._interval is None:
            try:
                self._interval = interval.Interval(f"{self.interval_quality}{self.interval_number}")
            except interval.IntervalException:
                self.interval_number = random.choice(self.interval_numbers)

    def _generate_question(self):
        self._question = f"How many semitones are there in a/an {self._interval.niceName}?"

    def _generate_answer(self):
        self._answer = self._interval.semitones

    def _generate_answer_options(self):
        self._answer_options = random_numbers_answer_options(self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = [{'prompt': "What is another name for a semitone?", 'answer': 'half step'},
                            {'prompt': f"How many half steps are there in a {self._interval.niceName}", 'answer': self.answer}]

    def _generate_question_type(self):
        self._question_type = 'semitones-in-interval'

    def _generate_question_params(self):
        self._question_params = {}