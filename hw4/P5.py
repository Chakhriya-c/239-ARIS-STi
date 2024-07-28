import numpy as np

def natresp(a, t, x0):
    return x0 * np.exp(a * t)
