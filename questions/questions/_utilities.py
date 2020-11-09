import random
from music21 import pitch, analysis, chord

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

diatonic_modes = ['dorian',
                  'phrygian',
                  'lydian',
                  'mixolydian',
                  'aeolian',
                  'locrian']

seventh_chord_qualities = ['major seventh chord',
                  'dominant seventh chord',
                  'minor seventh chord',
                  'half-diminished seventh chord',
                  'diminished seventh chord',
                  'dominant seventh flat five chord',
                  'augmented seventh chord']

# 'Messiaen\'s truncated mode 6',  Major 3rd, b5th, b7th

def random_pitch():
    return random.choice(pitch_names) + random.choice(accidentals)

def random_mode():
    return random.choice(diatonic_modes)

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

def random_answer_options_seventh_chords(len_of_list=4, correct_answer=None):
    random_answer_list = [correct_answer] if correct_answer else []
    while len(random_answer_list) < len_of_list:
        random_quality = random.choice(seventh_chord_qualities)
        if random_quality not in random_answer_list:
            random_answer_list.append(random_quality)
    random.shuffle(random_answer_list)
    return random_answer_list

def random_root_position_major_triad():
    c = chord.Chord(['C','E','G'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_minor_triad():
    c = chord.Chord(['C', 'E-', 'G'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_diminished_triad():
    c = chord.Chord(['C', 'E-', 'G-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_root_position_augmented_triad():
    c = chord.Chord(['C', 'E', 'G#'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_triads = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_triads)

def random_major_seventh_chord():
    c = chord.Chord(['C','E','G','B'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_dominant_seventh_chord():
    c = chord.Chord(['C','E','G','B-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_half_diminished_seventh_chord():
    c = chord.Chord(['C','E-','G-','B-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_minor_seventh_chord():
    c = chord.Chord(['C','E-','G','B-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_diminished_seventh_chord():
    c = chord.Chord(['C','E-','G-','B--'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_dominant_seventh_flat_5_chord():
    c = chord.Chord(['C','E','G-','B-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)

def random_augmented_seventh_chord():
    c = chord.Chord(['C','E','G#','B-'])
    tc = analysis.transposition.TranspositionChecker(c)
    transposed_seventh_chords = tc.getChordsOfDistinctTranspositions()
    return random.choice(transposed_seventh_chords)


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