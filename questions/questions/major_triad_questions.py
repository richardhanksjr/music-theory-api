import random
from music21 import key
from .questions import Question
from ._utilities import (scale_degrees, random_pitch, random_answer_options_pitch)

class SimpleMajorTriad(Question):

    def __init__(self, tonic=None, chord_degree=None):
        self.tonic = tonic if tonic else random_pitch()
        self.chord_degree = chord_degree if chord_degree else random.choice([1, 3, 5])
        super().__init__()




# Rich's question
class SimpleScaleDegreeMinor(Question):

    def __init__(self, tonic=None, scale_degree_index=None):
        self.tonic = tonic if tonic else random_pitch()
        self.scale_degree_index = scale_degree_index if scale_degree_index else random.choice(range(8))
        super().__init__()

    def _generate_question(self):

        self.scale_degree = scale_degrees[int(self.scale_degree_index)]
        self.scale = key.Key(self.tonic, 'minor')
        self._question = f"What is the {self.scale_degree['name']} scale degree " \
                         f"of {self.scale.getTonic().unicodeName} natural {self.scale.mode.capitalize()}?"

    def _generate_answer(self):
        scale = key.Key(self.tonic, 'minor')
        self._answer = scale.pitches[int(self.scale_degree_index)].unicodeName

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the root of this key?', 'answer': self.scale.getTonic().unicodeName},
                           {'prompt': f'Starting on {self.scale.getTonic().unicodeName},'
                                      f' count up the natural {self.scale.mode.capitalize()} scale until you reach the '
                                      f'{self.scale_degree["name"]} scale degree. What is this note?',
                            'answer': self._answer})

    def _generate_question_type(self):
        self._question_type =  'simple-scale-degree-natural-minor'

    def _generate_question_params(self):
        self._question_params =  {}