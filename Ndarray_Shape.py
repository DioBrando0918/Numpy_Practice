import numpy as np

data = np.ones(10)
data.shape  # (10,) 取得維度

data = np.array([
    [2, 4, 1],
    [1, 5, 0]
])
print(data.T)  # 轉置

data = np.array([
    [
        [2, 1, 3], [1, 2, 3]
    ],
    [
        [0, 2, 1], [8, 9, 10]
    ]
])
# print(data.ravel())  # 資料扁平化,轉成一維陣列

print(data.reshape(1, 1, 1, 1, 1, 1, 12))  # 重塑資料形狀,資料數量必須一樣
