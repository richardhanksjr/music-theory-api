import random
from .questions import Question
from ._utilities import (triad_degrees, random_answer_options_pitch,
                         random_root_position_major_triad,
                         random_root_position_minor_triad,
                         random_root_position_diminished_triad,
                         random_root_position_augmented_triad)


class SimpleMajorTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_major_triad()
        if 'natural' not in self.triad.root().fullName:
            self.root = self.triad.root().unicodeName
        else:
            self.root = self.triad.root().name
        if 'natural' not in self.triad.third.fullName:
            self.third = self.triad.third.unicodeName
        else:
            self.third = self.triad.third.name
        if 'natural' not in self.triad.fifth.fullName:
            self.fifth = self.triad.fifth.unicodeName
        else:
            self.fifth = self.triad.fifth.name
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.root} major triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.third
        else:
            self._answer = self.fifth

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': f'Counting {self.root} as \"one\", '
                            f'count up the minor scale until you reach the '
                            f'{self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},
                            {'prompt': 'What is the root of this triad?',
                             'answer': f"{self.root}"},)

    def _generate_question_type(self):
        self._question_type = 'simple-major-triad'

    def _generate_question_params(self):
        self._question_params = {}


class SimpleMinorTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_minor_triad()
        if 'natural' not in self.triad.root().fullName:
            self.root = self.triad.root().unicodeName
        else:
            self.root = self.triad.root().name
        if 'natural' not in self.triad.third.fullName:
            self.third = self.triad.third.unicodeName
        else:
            self.third = self.triad.third.name
        if 'natural' not in self.triad.fifth.fullName:
            self.fifth = self.triad.fifth.unicodeName
        else:
            self.fifth = self.triad.fifth.name
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} of a {self.root} minor triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.third
        else:
            self._answer = self.fifth

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': f'Counting {self.root} as \"one\", '
                            f'count up the minor scale until you reach the '
                            f'{self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},
                            {'prompt': 'What is the root of this triad?',
                             'answer': f"{self.root}"},)

    def _generate_question_type(self):
        self._question_type = 'simple-minor-triad'

    def _generate_question_params(self):
        self._question_params = {}


class SimpleDiminishedTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_diminished_triad()
        if 'natural' not in self.triad.root().fullName:
            self.root = self.triad.root().unicodeName
        else:
            self.root = self.triad.root().name
        if 'natural' not in self.triad.third.fullName:
            self.third = self.triad.third.unicodeName
        else:
            self.third = self.triad.third.name
        if 'natural' not in self.triad.fifth.fullName:
            self.fifth = self.triad.fifth.unicodeName
        else:
            self.fifth = self.triad.fifth.name
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.root} diminished triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.third
        else:
            self._answer = self.fifth

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': f'Counting {self.root} as \"one\", '
                            f'count the number of alphabetical letters on your fingers while thinking the note names ' 
                            f'until you reach the {self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},
                           {'prompt': 'An diminished triad is built by stacking two minor thirds. How many '
                            'semitones/half steps are in a major third?',
                            'answer': '4'},
                            {'prompt': 'What is the relationship of a chord degree to it\'s root is based on?',
                            'answer': 'How many alphabetical letters separate the root from the chord degree'
                            ' counting the root as \"one\".'})

    def _generate_question_type(self):
        self._question_type = 'simple-minor-triad'

    def _generate_question_params(self):
        self._question_params = {}


class SimpleAugmentedTriad(Question):

    def __init__(self, triad=None, chord_degree=None):
        self.triad = triad if triad else random_root_position_augmented_triad()
        if 'natural' not in self.triad.root().fullName:
            self.root = self.triad.root().unicodeName
        else:
            self.root = self.triad.root().name
        if 'natural' not in self.triad.third.fullName:
            self.third = self.triad.third.unicodeName
        else:
            self.third = self.triad.third.name
        if 'natural' not in self.triad.fifth.fullName:
            self.fifth = self.triad.fifth.unicodeName
        else:
            self.fifth = self.triad.fifth.name
        self.chord_degree = chord_degree if chord_degree else random.choice(['third', 'fifth'])
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the {self.chord_degree} " \
                         f" of a {self.root} augmented triad?"

    def _generate_answer(self):
        if self.chord_degree == triad_degrees[1]:
            self._answer = self.third
        else:
            self._answer = self.fifth

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_pitch(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': f'Counting {self.root} as \"one\", '
                            f'count the number of alphabetical letters on your fingers while thinking the note names ' 
                            f'until you reach the {self.chord_degree} scale degree. What is this note?',
                            'answer': self._answer},
                           {'prompt': 'An augmented triad is built by stacking two major thirds. How many '
                            'semitones/half steps are in a major third?',
                            'answer': '4'},
                            {'prompt': 'What is the relationship of a chord degree to it\'s root is based on?',
                            'answer': 'How many alphabetical letters separate the root from the chord degree'
                            ' counting the root as \"one\".'})

    def _generate_question_type(self):
        self._question_type = 'simple-diminished-triad'

    def _generate_question_params(self):
        self._question_params = {}