import numpy as np

def gimme(input_array):
    # Implement this function
    array_sort = sorted(input_array)
    mid = array_sort[1]
    return input_array.index(mid)