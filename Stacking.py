import numpy as np

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])  # 2x3

arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])  # 2x3

result = np.vstack((arr1, arr2))
"""
2+2=4
4x3
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""
print(result)

result = np.hstack((arr1,arr2))
"""
3+3=7
2x6
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
"""
print(result)
