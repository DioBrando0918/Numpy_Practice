import numpy as np

""""
逐元運算
"""
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
result = data1 + data2  # [ 4  5 16]
result = data1 * data2  # [ 3  6 60]
print(data1 > data2)  # [ True False  True]
print(data1 == data2)  # [False False False]

"""
矩陣運算
"""
data1 = np.array(
    [
        [1, 3]
    ]
)  # 1x2
data2 = np.array([
    [2, -1, 3],
    [-2, 4, 1]
])  # 2x3
result = data1.dot(data2)  # 內積
print(result)

result = data1 @ data2  # 內積
print(result)

result = np.outer(data1, data2)  # 外積 2x6
print(result)

"""
統計運算
"""
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])
print(data.sum())  # 總和 把多維陣列裡的所有元素做加總 16
result = data.max()  # 找出最大值 8
result = data.min()  # 找出最小值 -5
rerult = data.mean()  # 平均數
rerult = data.std()  # 標準差
result = data.sum(axis=0)  # 針對column [-3  4 15]
result = data.sum(axis=1)  # 針對row [10  6]
result = data.max(axis=0)  # [2 3 8]
result = data.max(axis=1)  # [7 8]
result = data.mean(axis=0)  # [-1.5  2.   7.5]
result = data.mean(axis=1)  # [3.33333333 2.        ]
result = data.cumsum()  # 逐值累加 [ 2  3 10  5  8 16]
result = data.cumsum(axis=0) # [[ 2  1  7],[-3  4 15]]

print(result)
