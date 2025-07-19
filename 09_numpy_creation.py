import numpy as np
#對於上面建立的每一個陣列，都把它自己以及它的 .shape, .ndim, .dtype 屬性印出來
def npPrintData(arr):
    print("形狀:", arr.shape)
    print("維度:", arr.ndim)
    print("元素的資料型態 (.dtype):", arr.dtype)
    print("-------------------------------------")
#使用 np.arange() 建立一個包含 1 到 20 之間所有偶數的陣列。(提示：arange 的第三個參數是 step 步長)
arr_arange = np.arange(2,21,2)
print("類似for的陣列: ", arr_arange)
npPrintData(arr_arange)

# 使用 np.zeros() 建立一個 4x5 (4列5行) 的二維陣列。
arr_zeros = np.zeros((4, 5))
print("用0畫出形狀的陣列:\n", arr_zeros) 
npPrintData(arr_zeros)

#使用 np.linspace() 建立一個從 0 到 1，總共有 11 個元素的陣列 (也就是 0, 0.1, 0.2, ..., 1.0)
arr_linspace = np.linspace(0, 1, 11)
print("將0到1分爲11段的陣列: ", arr_linspace)
npPrintData(arr_linspace)



