# import random
# from music21 import key
# from .questions import Question
# from _utilities import (pitch_names, accidentals, scale_degrees, random_pitch, random_answer_options_pitch)
#
#
# class SimpleScaleDegreeMajor(Question):
#
#     def __init__(self, **kwargs):
#         self.tonic = kwargs.get('tonic')
#         # self.scale_degree_index = kwargs.get('scale_degree_index')
#         self.scale_degree_index = None
#         self.scale_degree = None
#         self._question = None
#         self._answer = None
#         self._answer_options = None
#         self._help_steps = None
#         self.scale = None
#         self._key = None
#         self._response = None
#         super().__init__()
#
#
#     def _generate_answer(self):
#         scale = key.Key(self.tonic)
#         self._answer = scale.pitches[self.scale_degree_index].unicodeName
#
#     def _generate_answer_options(self):
#         self._answer_options = random_answer_options_pitch(correct_answer=self._answer)
#
#     def _generate_question(self):
#         if not self.tonic:
#             self.tonic = random_pitch()
#         if not self.scale_degree_index:
#             self.scale_degree_index = random.choice(range(8))
#         self.scale_degree = scale_degrees[self.scale_degree_index]
#         self.scale = key.Key(self.tonic)
#         self._question = f"What is the {self.scale_degree['name']} scale degree " \
#                          f"of {self.scale.getTonic().unicodeName} {self.scale.mode.capitalize()}?"
#
#     def _generate_help_steps_array(self):
#         self._help_steps = ({'prompt': 'What is the root of this key?', 'answer': self.scale.getTonic().unicodeName},
#                            {'prompt': f'Starting on {self.scale.getTonic().unicodeName},'
#                                       f' count up the {self.scale.mode.capitalize()} scale until you reach the '
#                                       f'{self.scale_degree["name"]} scale degree. What is this note?',
#                             'answer': self._answer})
#
#     @property
#     def question(self):
#         return self._question
#
#     @property
#     def answer_options(self):
#         return self._answer_options
#
#     @property
#     def answer(self):
#         return self._answer
#
#     @property
#     def question_type(self):
#         return 'simple-scale-degree-major'
#
#     @property
#     def question_params(self):
#         return {'question_type': self.question_type,
#                 'tonic': self.tonic, 'scale_degree_index': self.scale_degree_index}
#
#     @property
#     def help_steps(self):
#         return self._help_steps