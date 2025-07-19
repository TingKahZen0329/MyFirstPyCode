# 在檔案中，import numpy as np
import numpy as np

# 建立一個包含 [10, 20, 30, 40, 50] 的 Python list
my_list = [10, 20, 30, 40, 50]

# 將這個 list 轉換成一個 NumPy array，並把它印出來。
my_array = np.array(my_list)
print("這是一個 NumPy array:", my_array)


# 對這個 array 進行一次「向量化運算」，例如讓裡面每個數字都加上 100
my_array = my_array + 100

#將運算後的新 array 印出來
print("用 NumPy 直接運算的結果:", my_array)