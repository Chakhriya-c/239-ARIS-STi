import numpy as np

def normalize(v):
    norm = np.linalg.norm(v)
    unit_vector = v / norm
    return unit_vector