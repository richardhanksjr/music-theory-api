from music21 import key
from .questions import Question
from ._utilities import (random_mode, random_pitch, random_answer_options_accidentals)


class ModalKeySignatures(Question):

    def __init__(self, mode=None, parent_scale=None, key_sig=None):
        pitch = random_pitch()
        m = random_mode()
        self.mode = mode if mode else key.Key(pitch, m)
        self.key_signature = self.mode.sharps
        key_sig = key_sig if key_sig else key.KeySignature(self.key_signature)
        self.parent_scale = parent_scale if parent_scale else key_sig.getScale('major')
        self.parent_scale_name = self.parent_scale.tonic.unicodeName if self.parent_scale.tonic.accidental else self.parent_scale.tonic.name
        super().__init__()


    def _generate_question(self):
        # handle case of naturals
        mode_name = self.mode.tonic.unicodeName if self.mode.tonic.accidental else self.mode.tonic.name
        self._question = f"What is the key signature of {mode_name} {self.mode.type}?"


    def _generate_answer(self):
        if self.key_signature == 0:
            self._answer = "No sharps or flats"
        elif self.key_signature < 0:
            number_of_flats = -(self.key_signature)
            self._answer = f"{number_of_flats} flats"
        else:
            self._answer = f"{self.key_signature} sharps"



    def _generate_answer_options(self):
        self._answer_options = random_answer_options_accidentals(correct_answer=self._answer)


    def _generate_help_steps_array(self):
        if self.key_signature == 0:
            ks = "No sharps or flats."
        elif self.key_signature < 0:
            number_of_flats = -(self.key_signature)
            ks = f"{number_of_flats} flats"
        else:
            ks = f"{self.key_signature} sharps."
        self._help_steps = ({'prompt': f'What is the key signature of {self.parent_scale_name} major',
                            'answer': ks},
                            {'prompt': 'What is the parent major scale of this mode?',
                             'answer': f"{self.parent_scale_name} major"},)

    def _generate_question_type(self):
        self._question_type = 'modal-key-signatures'


    def _generate_question_params(self):
        self._question_params = {'question_type': self.question_type,
                'mode': self.mode.name, 'parent_scale': self.parent_scale_name}
