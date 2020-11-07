from music21 import interval
from .questions import Question
from ._utilities import (random_major_seventh_chord,
                         random_minor_seventh_chord,
                         random_dominant_seventh_chord,
                         random_half_diminished_seventh_chord,
                         random_diminished_seventh_chord,
                         random_dominant_seventh_flat_5_chord,
                         random_augmented_seventh_chord,
                         random_answer_options_seventh_chords)


class SimpleMajorSeventh(Question):

    def __init__(self, chord=None, chord_quality=None):
        self.chord = chord if chord else random_major_seventh_chord()
        if 'natural' not in self.chord.root().fullName:
            self.root = self.chord.root().unicodeName
        else:
            self.root = self.chord.root().name
        if 'natural' not in self.chord.third.fullName:
            self.third = self.chord.third.unicodeName
        else:
            self.third = self.chord.third.name
        if 'natural' not in self.chord.fifth.fullName:
            self.fifth = self.chord.fifth.unicodeName
        else:
            self.fifth = self.chord.fifth.name
        if 'natural' not in self.chord.seventh.fullName:
            self.seventh = self.chord.seventh.unicodeName
        else:
            self.seventh = self.chord.seventh.name
        self.chord_quality = chord_quality if chord_quality else self.chord.commonName
        super().__init__()

    def _generate_question(self):
        self._question = f"What is the quality of this chord,\
                           spelled bottom up {self.root}, {self.third}, {self.fifth}, {self.seventh}"

    def _generate_answer(self):
        self._answer = self.chord_quality

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_seventh_chords(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        # might have to say self.chord.root() instead of self.root
        root_to_third = interval.Interval(self.chord.third, self.chord.root())
        root_to_fifth = interval.Interval(self.chord.fifth, self.chord.root())
        root_to_seventh = interval.Interval(self.chord.seventh, self.chord.root())
        self._help_steps = ({'prompt': 'What is the interval quality from the root to the fifth?',
                            'answer': root_to_fifth.niceName},
                            {'prompt': 'What is the interval quality from the root to the seventh?',
                             'answer': root_to_seventh.niceName},
                            {'prompt': 'What is the interval quality from the root to the third?',
                             'answer': root_to_third.niceName},)

    def _generate_question_type(self):
        self._question_type = 'simple-major-seventh'

    def _generate_question_params(self):
        self._question_params = {}

