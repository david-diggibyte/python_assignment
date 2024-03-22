import numpy as np
def array_operations(arr):
    #np.set_printoptions(legacy='1.13')
    floor = np.floor(arr)
    ceil = np.ceil(arr)
    rint = np.rint(arr)
    return f"{floor}\n{ceil}\n{rint}"

