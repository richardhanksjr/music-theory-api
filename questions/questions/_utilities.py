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

def random_pitch():
    return random.choice(pitch_names) + random.choice(accidentals)


def random_answer_options_pitch(len_of_list=4, correct_answer=None):
    random_answer_list = [correct_answer] if correct_answer else []
    while len(random_answer_list) < len_of_list:
        random_pitch_inner = pitch.Pitch(random_pitch()).unicodeName
        if random_pitch_inner not in random_answer_list:
            random_answer_list.append(random_pitch_inner)
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