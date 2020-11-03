import random
from .questions import Question
from ._utilities import (triad_degrees, random_answer_options_pitch, random_root_position_major_triad, random_root_position_minor_triad, random_root_position_diminished_triad, random_root_position_augmented_triad)

class SimpleMajorTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_major_triad()
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.triad.root().name} major triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.triad.third.name
        else:
            self._answer = self.triad.fifth.name

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the root of this triad?', 'answer': f"{self.triad.root().name}"},
                           {'prompt': f'Starting on {self.triad.root().name},'
                                      f' and counting that note as \"one\", count up the major scale until you reach the '
                                      f'{self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer})

    def _generate_question_type(self):
        self._question_type = 'simple-major-triad'

    def _generate_question_params(self):
        self._question_params =  {}

class SimpleMinorTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_minor_triad()
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.triad.root().name} minor triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.triad.third.name
        else:
            self._answer = self.triad.fifth.name

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the root of this triad?', 'answer': f"{self.triad.root().name}"},
                           {'prompt': f'Starting on {self.triad.root().name},'
                                      f' and counting that note as \"one\", count up the minor scale until you reach the '
                                      f'{self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer})

    def _generate_question_type(self):
        self._question_type = 'simple-minor-triad'

    def _generate_question_params(self):
        self._question_params =  {}

class SimpleDiminishedTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_diminished_triad()
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.triad.root().name} diminished triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.triad.third.name
        else:
            self._answer = self.triad.fifth.name

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the relationship of a chord degree to it\'s root is based on?',
                             'answer': 'How many alphabetical letters separate the root from the chord degree counting the root as \"one\".'},
                            {
                            'prompt': 'A diminished triad is built by stacking two minor thirds. How many semitones/half steps are in a minor third?',
                            'answer': '3'},
                           {'prompt': f' Starting on {self.triad.root().name}, and counting that note as \"one\", count the number of alphabetical letters on your fingers while thinking the note names ' 
                                      f'until you reach the {self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},)

    def _generate_question_type(self):
            self._question_type = 'simple-minor-triad'

    def _generate_question_params(self):
            self._question_params = {}

class SimpleAugmentedTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_augmented_triad()
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.triad.root().name} augmented triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.triad.third.name
        else:
            self._answer = self.triad.fifth.name

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is the relationship of a chord degree to it\'s root is based on?',
                             'answer': 'How many alphabetical letters separate the root from the chord degree counting the root as \"one\".'},
                            {'prompt': 'An augmented triad is built by stacking two major thirds. How many semitones/half steps are in a major third?',
                            'answer': '4'},
                           {'prompt': f'Starting on {self.triad.root().name},'
                                      f' and counting that note as \"one\", count the number of alphabetical letters on your fingers while thinking the note names ' 
                                      f'until you reach the {self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},)

    def _generate_question_type(self):
        self._question_type = 'simple-diminished-triad'

    def _generate_question_params(self):
        self._question_params = {}