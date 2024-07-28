import numpy as np

def plane3d(Px, Py, n, k):
    nx, ny, nz = n
    z = (k - nx * Px - ny * Py) / nz
    return z
