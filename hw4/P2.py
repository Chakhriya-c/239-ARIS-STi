import numpy as np
def marrange(A, B):
    A = A.reshape(-1, 1)
    B = B.reshape(1, -1)
    C = A * B
    return C
