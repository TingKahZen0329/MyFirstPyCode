import numpy as np
#首先，使用 np.arange(1, 21) 建立一個從 1 到 20 的一維陣列。
#接著，使用 .reshape((4, 5)) 這個新函式，將它變成一個 4x5 的二維陣列。
base_array = np.arange(1, 21).reshape((4, 5))
print(base_array)

# 選取出數字 13
print("選取出數字: ",base_array[2,2])

# 選取出第二列的所有數字 (也就是 [6, 7, 8, 9, 10])
print("選取出第二列的所有數字: ",base_array[1,:])

# 選取出第三行的所有數字 (也就是 [3, 8, 13, 18])
print("選取出第三行的所有數字: ",base_array[:,2])

# 選取出右下角的 2x2 矩陣 (也就是 [[14, 15], [19, 20]])
print("選取出右下角的 2x2 矩陣:\n",base_array[2:4,3:5])
