import numpy as np

def rmse(yp, y):
    return np.sqrt(np.mean((yp - y) ** 2))
