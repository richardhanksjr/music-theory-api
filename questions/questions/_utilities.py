import random
from music21 import pitch, analysis

pitch_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
accidentals = ['-', '--', '#', '##', '']
scale_degrees = [{'name': "first"},
                 {'name': "second"},
                 {'name': "third"},
                 {'name': "fourth"},
                 {'name': "fifth"},
                 {'name': "sixth"},
                 {'name': "seventh"},
                 {'name': "eighth"}]

triad_degrees = ["root", "third", "fifth"]

diatonic_modes = ['dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian']
interval_qualities = ['P', 'M', 'm', 'd', 'A']
qualities = ['Major', 'Minor', 'Augmented', 'Diminished', 'Perfect']
interval_qualities_full_name = ['perfect', 'major', 'minor', 'diminished', 'augmented']



def random_interval_qualities(len_of_list=4, correct_answer=None):
    intervals = [correct_answer] if correct_answer else []
    while len(intervals) < len_of_list:
        interval = random.choice(interval_qualities_full_name)
        if interval not in intervals:
            intervals.append(interval)
    random.shuffle(intervals)
    return intervals


def random_pitch():
    return random.choice(pitch_names) + random.choice(accidentals)


def random_mode():
    return random.choice(diatonic_modes)

def random_pitch_with_octave(min_octave=None, max_octave=None):
    min_octave = min_octave if min_octave is not None else 1
    max_octave = max_octave if max_octave is not None else 4

    return f"{random_pitch()}{random.randint(min_octave, max_octave)}"


def random_intervals_with_octaves(correct_answer, len_of_list=4):
    correct_answer_list = [correct_answer]
    incorrect_answers = []
    while len(incorrect_answers) < len_of_list - 1:
        random_interval = f"{random.choice(interval_qualities)}{random.randint(1, 40)}"
        while random_interval in incorrect_answers or random_interval in correct_answer_list:
            random_interval = f"{random.choice(interval_qualities)}{random.randint(1, 40)}"
        incorrect_answers.append(random_interval)
    answer_options = correct_answer_list + incorrect_answers
    random.shuffle(answer_options)
    return answer_options


def random_answer_options_pitch(len_of_list=4, correct_answer=None):
    random_answer_list = [correct_answer] if correct_answer else []
    while len(random_answer_list) < len_of_list:
        random_pitch_inner = pitch.Pitch(random_pitch()).unicodeName
        if random_pitch_inner not in random_answer_list:
            random_answer_list.append(random_pitch_inner)
    random.shuffle(random_answer_list)
    return random_answer_list

def random_answer_options_accidentals(len_of_list=4, correct_answer=None):
    random_answer_list = [correct_answer] if correct_answer else []
    while len(random_answer_list) < len_of_list:
        random_number = random.choice(range(7))
        random_sign = random.choice(['sharps', 'flats'])
        random_accidentals = f"{random_number} {random_sign}"
        if random_accidentals not in random_answer_list:
            random_answer_list.append(random_accidentals)
    random.shuffle(random_answer_list)
    return random_answer_list

def random_root_position_major_triad():
    pList = [pitch.Pitch('C'), pitch.Pitch('E'), pitch.Pitch('G')]
    tc = analysis.transposition.TranspositionChecker(pList)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_minor_triad():
    pList = [pitch.Pitch('C'), pitch.Pitch('E-'), pitch.Pitch('G')]
    tc = analysis.transposition.TranspositionChecker(pList)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_diminished_triad():
    pList = [pitch.Pitch('C'), pitch.Pitch('E-'), pitch.Pitch('G-')]
    tc = analysis.transposition.TranspositionChecker(pList)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_augmented_triad():
    pList = [pitch.Pitch('C'), pitch.Pitch('E'), pitch.Pitch('G#')]
    tc = analysis.transposition.TranspositionChecker(pList)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)


def random_numbers_answer_options(correct_answer, len_of_list=4):
    highest_number = 22
    initial_list = [correct_answer]
    incorrect_answers = []
    while len(incorrect_answers) < len_of_list - 1:
        random_int = random.randint(1, highest_number)
        while random_int in incorrect_answers or random_int in initial_list:
            random_int = (random_int + 1) % highest_number
        incorrect_answers.append(random_int)
    answer_options = initial_list + incorrect_answers
    random.shuffle(answer_options)
    return answer_options


def random_answer_options_quality(len_of_list=4, correct_answer=None):
    random_answer_list = [correct_answer] if correct_answer else []
    while len(random_answer_list) < len_of_list:
        choices = random.choice(qualities)
        if choices not in random_answer_list:
            random_answer_list.append(choices)
    random.shuffle(random_answer_list)
    return random_answer_list