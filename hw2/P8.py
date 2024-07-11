# DONE 

def diatonic(scale_key):
    offsets = [0, 2, 4, 5, 7, 9, 11]  
    notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']

    diatonic_notes = []
    for offset in offsets:
        note_num = (scale_key - 1 + offset) % 12
        diatonic_notes.append(note_num + 1)

    scale_note = notes[scale_key - 1]
    print(f"Diatonic notes in the key of {scale_note} ( {scale_key} )")

    for note in diatonic_notes:
        note_name = notes[note - 1]
        if len(note_name) == 1:
            print(f" {note_name}", end=" ")
        else:
            print(f"{note_name}", end=" ")
    print()

    print(" ".join(f" {note:1}" if note < 10 else f"{note:0}" for note in diatonic_notes))

scale_key = int(input("Enter the key [1-12]:"))
diatonic(scale_key)
