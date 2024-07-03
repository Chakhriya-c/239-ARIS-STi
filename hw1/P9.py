first_note = int(input("The first note:"))
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

indices = [(first_note - 1) % 7, (first_note + 1) % 7, (first_note + 3) % 7]

note_list = [notes[i] for i in indices]

triad_indices = " ".join(map(str, [idx + 1 for idx in indices]))

triad_notes = ",".join(note_list)

print("Triad: ", triad_indices)
print(triad_notes)
