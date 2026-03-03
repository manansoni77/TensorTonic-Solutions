import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    if type(x) == list:
        return [sigmoid(y) for y in x]
    else:
        return 1 / (1 + np.exp(-1 * x))
    pass