#!/usr/bin/env python3
print("Give me a root note and I'll give you the major chord.")


def ask_for_note():
    # Validate it.
    return "B"

# Ask for a root note.
note = ask_for_note()

def get_major_chord(root_note):
    notes = [
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

    index = notes.index(root_note)

    # reorganize the list so the root is at the beginning
    before = notes[:index]
    notes = notes[index:]
    notes.extend(before)

    third = notes[4]
    fifth = notes[7]
    chord = '{:s}-{:s}-{:s}'.format(root_note, third, fifth)
    return chord

chord = get_major_chord(note)

# Give the major chord.
print('The major chord for the root {:s} is {:s}.'.format(note, chord))
