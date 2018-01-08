#!/usr/bin/env python3
print("Give me a root note.")

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

def interpret_note_variant(note):
    """Convert shorthand and weird names to our NOTES."""
    note = note.replace('+', '♯')
    note = note.replace('-', '♭')
    note = note.upper()
    weird_variations = {
            'A♭': 'G♯',
            'A♯': 'B♭',
            'D♭': 'C♯',
            'D♯': 'E♭',
            'G♭': 'F♯',
            }
    if (note in weird_variations):
        return weird_variations[note]
    return note

def ask_for_note():
    while True:
        note = interpret_note_variant(input("root note: "))
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
    return 'major', chord

def get_minor_chord(root_note):
    shifted_notes = shift_list(NOTES, root_note)
    third = shifted_notes[3]
    fifth = shifted_notes[7]
    chord = '{:s}-{:s}-{:s}'.format(root_note, third, fifth)
    return 'minor', chord

note = ask_for_note()

chord_types = [
        get_major_chord,
        get_minor_chord,
        ]

for chord_type in chord_types:
    chord_type_name, chord = chord_type(note)
    print('The {:s} chord for the root {:s} is {:s}.'.format(chord_type_name, note, chord))
