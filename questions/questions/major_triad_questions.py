import random
from music21 import chord, analysis
from .questions import Question
from ._utilities import (triad_degrees, random_answer_options_pitch, random_root_position_major_triad)

class SimpleMajorTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_major_triad()
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree}" \
                         f"of a {self.triad.root()} major triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.triad.third
        else:
            self._answer = self.triad.fifth

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the root of this triad?', 'answer': self.triad.root()},
                           {'prompt': f'Starting on {self.triad.root()},'
                                      f' count up the {self.triad.root()} major until you reach the '
                                      f'{self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer})

    def _generate_question_type(self):
        self._question_type = 'simple-major-triad'

    def _generate_question_params(self):
        self._question_params =  {}


