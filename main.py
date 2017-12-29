#!/usr/bin/env python3
print("Give me a root note and I'll give you the major chord.")


def ask_for_note():
    # Validate it.
    return "C"

# Ask for a root note.
note = ask_for_note()

def get_major_chord(root_note):
    return "C-E-G"

chord = get_major_chord(note)

# Give the major chord.
print("The major chord for the root", note, "is", chord, ".")
