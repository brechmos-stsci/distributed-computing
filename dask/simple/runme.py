import numpy as np

from dask.distributed import Client
client = Client('127.0.0.1:8786')

def sum_matrix(A):
    """
    Slightly inefficient function.
    """ 
    total = 0
    for row in range(A.shape[0]):
        for col in range(A.shape[1]):
            for z in range(A.shape[2]):
                total += A[row, col, z]
    return total

#
# Launch the computations on the cluster.  
#    This returns a Future immediately, not the answer. A future is a
#    lightweight token refering to results on the cluster.
#

proc_futures = client.map(sum_matrix, [np.random.random((256, 256, 24)) for x in range(10)])
print(proc_futures)
print('')

while not all(x.status == 'finished' for x in proc_futures):
    print('\r{}'.format(list(x.status for x in proc_futures)), end='')
print('\n')

#
#  Results of the computations stay on the cluster, so we have
#  to retrieve them when they are completed.
#
#  Results can be retrieved from a future or from the map. This
#  will block waiting for all the results of the map.
#

proc_results = client.gather(proc_futures)
print(proc_results)
