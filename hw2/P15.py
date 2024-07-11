# DONE
import math

def earthquake(event_list):
    for event in event_list:
        energy = 10**(4.8 + 1.5 * event[1])
        event.append(energy)
    return event_list