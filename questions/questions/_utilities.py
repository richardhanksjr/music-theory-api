import random
from music21 import pitch, chord

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

triad_tones = [{'name': "root"},
               {'name': "third"},
               {'name': "fifth"}]

cMajor = chord.Chord(["C3", "E3", "G3"])


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