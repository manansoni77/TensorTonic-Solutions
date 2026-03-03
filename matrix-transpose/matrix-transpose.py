import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    nr = len(A)
    nc = len(A[0])

    res = []
    for i in range(nc):
        res.append([0] * nr)

    for i in range(nr):
        for j in range(nc):
            res[j][i] = A[i][j]
            
    return np.array(res)
    pass
