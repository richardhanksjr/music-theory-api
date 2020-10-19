import random
from .questions import Question


class SimpleIntervalIs(Question):

    def _generate_answer(self):
        self._answer = "An interval that encompasses an octave or less"

    def _generate_answer_options(self):
        self._answer_options = ["A perfect interval", "A Major or minor interval",
                                "An interval that encompasses an octave or less",
                                "A consonant interval"]

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is a simple interval?',
                             'answer': 'an interval of one octave or less.'},)


    def _generate_question(self):
        self._question = "A SIMPLE INTERVAL is: "

    def _generate_question_type(self):
        self._question_type = "simple-interval-is"

    def _generate_question_params(self):
        self._question_params = {'question_type': self.question_type}


class InvertedQualityIs(Question):

    def __init__(self, interval_quality=None, same=None):
        self.interval_quality = interval_quality if interval_quality else random.choice(['major', 'minor', 'diminished', 'augmented', 'perfect'])
        self.same = same if same is not None else random.choice([True, False])
        self.formatted_remains = "remains" if self.same is True else "does NOT remain"
        super().__init__()

    def _generate_question(self):
        self._question = f"If a {self.interval_quality.lower()} interval is inverted it {self.formatted_remains} {self.interval_quality}"

    def _generate_answer(self):
        if self.interval_quality.lower() == 'perfect':
            self._answer = "True" if self.same is True else "False"
        else:
            self._answer = "False" if self.same is True else "True"

    def _generate_answer_options(self):
        self._answer_options = ["True", "False"]

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'How are interval qualities affected by inversion?',
                           'answer': 'Perfect -> Perfect, Major -> minor, minor -> Major, diminished '
                                     '-> Augmented, Augmented -> diminished'}, )

    def _generate_question_type(self):
        self._question_type = 'inverted_quality_is'

    def _generate_question_params(self):
        self._question_params = {}