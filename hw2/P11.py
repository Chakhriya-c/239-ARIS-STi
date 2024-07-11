# DONE

def perf_note(pnotes, coefficient):
    for note in pnotes:
        note_name = note[0]
        min_coefficient = note[1]
        max_coefficient = note[2]
        
        if min_coefficient <= coefficient <= max_coefficient:
            return note_name
    
    return None
