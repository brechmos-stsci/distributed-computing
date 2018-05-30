import numpy as np
from celery_conf import app

@app.task
def sum_matrix(Alist):
    """
    Slightly inefficient function.
    """ 
    A = np.array(Alist)
    total = 0
    for row in range(A.shape[0]):
        for col in range(A.shape[1]):
            for z in range(A.shape[2]):
                total += A[row, col, z]
    return total
