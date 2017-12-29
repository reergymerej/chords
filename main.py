#!/usr/bin/env python3
print("Give me a root note and I'll give you the major chord.")

NOTES = [
        'A',
        'B♭',
        'B',
        'C',
        'C♯',
        'D',
        'E♭',
        'E',
        'F',
        'F♯',
        'G',
        'G♯',
        ]

def validate_note(note):
    return note.upper() in NOTES

def ask_for_note():
    while True:
        note = input("root note: ").upper()
        if (validate_note(note)):
            return note
        else:
            print("I don't understand that note.")


def shift_list(the_list, item):
    """Reorganize list so item is at 0 index."""
    index = the_list.index(item)
    before = the_list[:index]
    the_list = the_list[index:]
    the_list.extend(before)
    return the_list

def get_major_chord(root_note):
    shifted_notes = shift_list(NOTES, root_note)
    third = shifted_notes[4]
    fifth = shifted_notes[7]
    chord = '{:s}-{:s}-{:s}'.format(root_note, third, fifth)
    return chord

note = ask_for_note()
chord = get_major_chord(note)
print('The major chord for the root {:s} is {:s}.'.format(note, chord))
