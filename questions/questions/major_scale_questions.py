import random
from music21 import key
from .questions import Question
from ._utilities import (scale_degrees, random_pitch, random_answer_options_pitch)


class SimpleScaleDegreeMajor(Question):

    def __init__(self, tonic=None, scale_degree_index=None, **kwargs):
        self.tonic = tonic if tonic else random_pitch()
        self.scale_degree_index = scale_degree_index if scale_degree_index else random.choice(range(8))
        self.scale_degree = scale_degrees[self.scale_degree_index]
        self.scale = key.Key(self.tonic)
        super().__init__()


    def _generate_answer(self):
        scale = key.Key(self.tonic)
        self._answer = scale.pitches[self.scale_degree_index].unicodeName

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_question(self):

        self._question = f"What is the {self.scale_degree['name']} scale degree " \
                         f"of {self.scale.getTonic().unicodeName} {self.scale.mode.capitalize()}?"

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the root of this key?', 'answer': self.scale.getTonic().unicodeName},
                           {'prompt': f'Starting on {self.scale.getTonic().unicodeName},'
                                      f' count up the {self.scale.mode.capitalize()} scale until you reach the '
                                      f'{self.scale_degree["name"]} scale degree. What is this note?',
                            'answer': self._answer})

    def _generate_question_type(self):
        self._question_type = 'simple-scale-degree-major'


    def _generate_question_params(self):
        self._question_params =  {'question_type': self.question_type,
                'tonic': self.tonic, 'scale_degree_index': self.scale_degree_index}
