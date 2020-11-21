import random
from music21 import interval, pitch, scale
from questions.questions.questions import Question
from ._utilities import (random_numbers_answer_options, random_pitch_with_octave,
                         random_intervals_with_octaves, random_interval_qualities, random_answer_options_quality, qualities,
                         random_pitch, scale_degrees)



class SemitonesInInterval(Question):
    interval_qualities = ['a', 'd', 'm', 'M', 'p']
    interval_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def __init__(self, interval_quality=None, interval_number=None):
        self.interval_quality = interval_quality if interval_quality else random.choice(self.interval_qualities)
        self.interval_number = interval_number if interval_number else random.choice(self.interval_numbers)
        self._generate_interval()
        super().__init__()

    def _generate_interval(self):
        self._interval = None
        while self._interval is None:
            try:
                self._interval = interval.Interval(f"{self.interval_quality}{self.interval_number}")
            except interval.IntervalException:
                self.interval_number = random.choice(self.interval_numbers)

    def _generate_question(self):
        self._question = f"How many semitones are there in a/an {self._interval.niceName}?"

    def _generate_answer(self):
        self._answer = self._interval.semitones

    def _generate_answer_options(self):
        self._answer_options = random_numbers_answer_options(self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = [{'prompt': "What is another name for a semitone?", 'answer': 'half step'},
                            {'prompt': f"How many half steps are there in a {self._interval.niceName}",
                             'answer': self.answer}]

    def _generate_question_type(self):
        self._question_type = 'semitones-in-interval'

    def _generate_question_params(self):
        self._question_params = {}


class IntervalRaisedLoweredIs(Question):
    directions = ['raised', 'lowered']
    MIN_NUM_OCTAVES = 2
    MAX_NUM_OCTAVES = 4

    # pylint: disable=too-many-arguments
    def __init__(self, lower_pitch=None, upper_pitch=None, lower_direction=None, upper_direction=None,
                 lower_pitch_num_octaves=None, upper_pitch_num_octaves=None):
        self._lower_pitch = pitch.Pitch(
            lower_pitch if lower_pitch is not None else random_pitch_with_octave(max_octave=2))
        self._upper_pitch = pitch.Pitch(
            upper_pitch if upper_pitch is not None else random_pitch_with_octave(min_octave=3))
        self._lower_direction = lower_direction if lower_direction is not None else random.choice(self.directions)
        self._upper_direction = upper_direction if upper_direction is not None else random.choice(self.directions)
        self._lower_pitch_num_octaves = lower_pitch_num_octaves if lower_pitch_num_octaves is not None else random.randint(
            self.MIN_NUM_OCTAVES, self.MAX_NUM_OCTAVES)
        self._upper_pitch_num_octaves = upper_pitch_num_octaves if upper_pitch_num_octaves is not None else random.randint(
            self.MIN_NUM_OCTAVES, self.MAX_NUM_OCTAVES)
        super().__init__()

    def _generate_question(self):
        self._question = f"The interval {self._lower_pitch.unicodeNameWithOctave} to {self._upper_pitch.unicodeNameWithOctave} becomes " \
                         f"which interval when {self._lower_pitch.unicodeNameWithOctave} is {self._lower_direction} " \
                         f"{self._lower_pitch_num_octaves} octave(s) and {self._upper_pitch.unicodeNameWithOctave} is " \
                         f"{self._upper_direction} {self._upper_pitch_num_octaves} octave(s)?"

    def _alter_pitch(self, pitch, num_octaves, direction):
        direction_modifier = "-" if direction == 'lowered' else ""
        for _ in range(num_octaves):
            pitch = pitch.transpose(f"{direction_modifier}P8")
        return pitch

    def _generate_answer(self):
        lower_pitch = self._alter_pitch(self._lower_pitch, self._lower_pitch_num_octaves, self._lower_direction)
        upper_pitch = self._alter_pitch(self._upper_pitch, self._upper_pitch_num_octaves, self._upper_direction)
        self._answer = interval.Interval(noteStart=lower_pitch, noteEnd=upper_pitch).name

    def _generate_answer_options(self):
        self._answer_options = random_intervals_with_octaves(self.answer)

    def _generate_help_steps_array(self):
        self._help_steps = [{
            'prompt': f"What is {self._lower_pitch.unicodeNameWithOctave} "
                      f"{self._lower_direction} {self._lower_pitch_num_octaves} octaves?",
            'answer': self._alter_pitch(self._lower_pitch, self._lower_pitch_num_octaves,
                                        self._lower_direction).unicodeNameWithOctave
            },
            {
                'prompt': f"What is {self._upper_pitch.unicodeNameWithOctave} "
                          f"{self._upper_direction} {self._upper_pitch_num_octaves} octaves?",
                'answer': self._alter_pitch(self._upper_pitch, self._upper_pitch_num_octaves,
                                            self._upper_direction).unicodeNameWithOctave
            },
            {
                'prompt': f"What is the interval between "
                          f"{self._alter_pitch(self._lower_pitch, self._lower_pitch_num_octaves, self._lower_direction).unicodeNameWithOctave} "
                          f"and {self._alter_pitch(self._upper_pitch, self._upper_pitch_num_octaves, self._upper_direction).unicodeNameWithOctave}?",
                'answer': self.answer
            }]

    def _generate_question_type(self):
        self._question_type = 'interval-raised-lowered-is'

    def _generate_question_params(self):
        self._question_params = {}



class InvertedInterval(Question):
    interval_numbers = range(2, 15)

    def __init__(self, interval_quality=None, interval_number=None):
        self.interval_quality = interval_quality if interval_quality else random.choice(qualities)
        self.interval_number = interval_number if interval_number else random.choice(self.interval_numbers)
        self._generate_interval()
        super().__init__()

    def _generate_interval(self):
        self._interval = None
        while self._interval is None:
            try:
                self._interval = interval.Interval(f"{self.interval_quality}{self.interval_number}")
            except interval.IntervalException:
                self.interval_number = random.choice(self.interval_numbers)

    def _generate_question(self):
        self._question = f"When inverted, a {self._interval.specificName} interval becomes:"

    def _generate_answer(self):
        self._answer = self._interval.complement.specificName

    def _generate_answer_options(self):
        self._answer_options = random_answer_options_quality(correct_answer=self._answer)

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'How are interval qualities affected by inversion?',
                        'answer': 'Perfect -> Perfect, Major -> minor, minor -> Major, diminished '
                                    '-> Augmented, Augmented -> diminished'}, )

    def _generate_question_type(self):
        self._question_type = 'inverted_interval'

    def _generate_question_params(self):
        self._question_params = {} 

class IntervalChangedByStepBecomesQuality(Question):

    INTERVAL_MAPPINGS = {'M': {'name': 'major', 'larger': 'augmented', 'smaller': 'minor'},
                         'm': {'name': 'minor', 'larger': 'major', 'smaller': 'diminished'},
                         'P': {'name': 'perfect', 'larger': 'augmented', 'smaller': 'diminished'} 
                        }

    def __init__(self, quality=None, direction=None):
        """

        :param quality: String in the form of "M", "m", or 'P'
        :param direction: String either "larger" or "smaller"
        """
        quality_key = quality if quality else random.choice(list(self.INTERVAL_MAPPINGS.keys()))
        self._quality = self.INTERVAL_MAPPINGS[quality_key]
        self._direction = direction if direction is not None else random.choice(["larger", "smaller"])
        super().__init__()

    def _generate_question(self):
        self._question = f"A {self._quality['name']} interval made {self._direction} by a half step becomes what" \
                         f" type of interval?"

    def _generate_answer(self):
        self._answer = self._quality[self._direction]

    def _generate_answer_options(self):
        self._answer_options = random_interval_qualities(correct_answer=self.answer)

    def _generate_help_steps_array(self):
        self._help_steps = [{'prompt': 'How are interval qualities changed by being transposed up a half step?', 
                             'answer': 'major -> augmented, minor -> major, perfect -> augmented'},
                            {'prompt': 'How are interval qualities changed by being transposed down by a half step?',
                             'answer': 'major -> minor, minor -> diminished, perfect -> diminished'}]

    def _generate_question_type(self):
        self._question_type = 'interval-changed-by-step-becomes-quality'

    def _generate_question_params(self):
        self._question_params = {}


class CompoundIntervalRelationship(Question):

    # pylint: disable=too-many-arguments, unused-argument
    def __init__(self, tonic=None, major_scale_tonic=None, scale_degree_index=None, major_scale_degree_index=None,
                 compound_interval_index=None):
        self.tonic = tonic if tonic else random_pitch()
        self.major_scale_tonic = tonic if tonic else random_pitch()
        self.scale_degree_index = scale_degree_index if scale_degree_index else random.choice(range(7))
        self.major_scale_degree_index = major_scale_degree_index if major_scale_degree_index else random.choice(range(8))
        self.compound_interval_index = compound_interval_index if compound_interval_index else random.choice(range(13,24))
        self.scale_degree = scale_degrees[self.scale_degree_index]
        self.major_scale_degree = scale_degrees[self.major_scale_degree_index]
        self.whole_tone = scale.WholeToneScale(self.tonic)
        self.major_scale = scale.MajorScale(self.major_scale_tonic)
        self.compound_interval = interval.Interval(self.compound_interval_index)
        super().__init__()

    def _generate_question(self):
        self._question = f"When compounded, the interval produced by combining the " \
                         f"{self.scale_degree['name']} scale degree of a/an {self.whole_tone.getTonic()} whole tone scale " \
                         f"with the {self.major_scale_degree['name']} scale degree of a/an {self.major_scale.getTonic().unicodeName} major scale " \
                         f"bears what relation to the interval of a {self.compound_interval.niceName}"

    def _generate_answer(self):
        n1 = self.whole_tone.pitches[self.scale_degree_index]
        n2 = self.major_scale.pitches[self.major_scale_degree_index]
        compare_first = interval.Interval(noteStart=n1, noteEnd=n2)
        compare_second = interval.Interval(self.compound_interval_index)
        if int(abs(compare_first.semitones)) <= 12:
            compounded_first = int(abs(compare_first.semitones)) + 12
        else:
            compounded_first = int(abs(compare_first.semitones))

        if compounded_first == int(compare_second.semitones):
            self._answer = 'It is the same quality'
        elif compounded_first < int(compare_second.semitones):
            self._answer = 'It is smaller'
        elif compounded_first > int(compare_second.semitones):
            self._answer = 'It is greater'
        else:
            self._answer = 'It is enharmonic'

    def _generate_answer_options(self):
        self._answer_options = ['It is greater', 'It is smaller', 'It is the same quality', 'It is enharmonic']

    def _generate_help_steps_array(self):
        n1 = self.whole_tone.pitches[self.scale_degree_index]
        n2 = self.major_scale.pitches[self.major_scale_degree_index]
        self._help_steps = [
            {
                'prompt': 'What is a compound interval?',
                'answer': 'An interval that is larger than an octave'
            },
            {
                'prompt': f"What is the {self.scale_degree['name']} scale degree of a/an {self.whole_tone.getTonic()} Whole Tone scale ",
                'answer': f"{n1.name}"
            },
            {
                'prompt': f"What is the {self.major_scale_degree['name']} scale degree of a/an {self.major_scale.getTonic().unicodeName} Major scale ",
                'answer': f"{n2.name}"
            },
            {
                'prompt': f"What is the compound interval between {n1}, and {n2}?",
                'answer': 'A minor 9th'
            },

        ]

    def _generate_question_type(self):
        self._question_type = 'compound_interval_relationship'

    def _generate_question_params(self):
        self._question_params = {}