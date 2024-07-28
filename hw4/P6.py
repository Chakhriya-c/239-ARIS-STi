import numpy as np

def innerprod(x, y):
    x_conj = np.conj(x)
    result = np.dot(x_conj, y)
    return result