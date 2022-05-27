import numpy as np

# 建立列表ndarray物件
array = np.array([3, 4, -5])
print(array)
print(array.size)  # len()
print(len(array))
# ------1D----------
np.array([3, 5, 4])  # 根據列表建立
np.empty(3)  # 建立資料未指定的一維陣列
np.zeros(3)  # 建立資料都是0的一維陣列
np.ones(3)  # 建立資料都是1一維陣列
np.arange(10)  # 建立連續資料的一維陣列
# ------2D----------
np.array([[1, 2],
          [3, 2],
          [5, 0]])  # 建立一個3x2的二維陣列
np.empty([3, 2])  # 建立一3x2的資料未指定的二維陣列
np.zeros([3, 2])  # 建立一3x2資料都是0的二維陣列
np.ones([3, 2])  # 建立一3x2資料都是1的二維陣列
# ------3D----------
np.array([
    [
        [5, 2, 4], [1, 2, 8]
    ], [
        [3, 8, 2], [4, 1, 3]
    ]
])  # 建立三維陣列
np.empty([2, 2, 3])  # 建立資料未指定的三維陣列
np.zeros([2, 2, 3])  # 建立資料為0的三維陣列

