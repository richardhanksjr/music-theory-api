from django.test import TestCase
from questions.questions.modal_key_signatures import ModalKeySignatures
from django.core.cache import cache
from questions.models import Question
from music21 import key
from questions.questions._utilities import random_pitch, random_mode, random_answer_options_accidentals


class ModalKeySignaturesTests(TestCase):
    def setUp(self):
        Question.objects.create(class_name='ModalKeySignatures')
        pitch = random_pitch()
        m = random_mode()
        mode = key.Key(pitch, m)
        key_signature = mode.sharps
        key_sig = key.KeySignature(key_signature)
        parent_scale = key_sig.getScale('major')
        self.question = ModalKeySignatures(mode=mode, parent_scale=parent_scale, key_sig=key_sig)

    def test_question_added_to_cache(self):
        cache_key = self.question.key
        question_from_cache = cache.get(cache_key)
        self.assertEqual(question_from_cache['question'], self.question.question)
        self.assertListEqual(question_from_cache['answer_options'], self.question.answer_options)
        self.assertEqual(question_from_cache['answer'], self.question.answer)

    def test_correct_weight(self):
        self.assertEqual(4, self.question.weight)

    def test_random_accidental_answer_options(self):
        options = random_answer_options_accidentals()
        self.assertEquals(len(options), 4)


