import numpy as np

def get_info(lst):
    arr = np.array(lst)
    info = {
        'shape': arr.shape,
        'dtype': arr.dtype
    }
    return arr, info