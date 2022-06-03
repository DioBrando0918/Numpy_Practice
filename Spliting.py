import numpy as np

arr = np.array(
    [
        [2, 4, 6, 8, 10, 12],
        [1, 3, 5, 7, 9, 11]
    ])

result = np.vsplit(arr, 2)
print(result)
"""
[array([[ 2,  4,  6,  8, 10, 12]]), array([[ 1,  3,  5,  7,  9, 11]])]
"""
result = np.hsplit(arr, 2)
print(result)
"""
[array([[2, 4, 6],
       [1, 3, 5]]), 
array([[ 8, 10, 12],
       [ 7,  9, 11]])]
"""
