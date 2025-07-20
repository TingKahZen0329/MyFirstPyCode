import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 從 scikit-learn 中匯入我們需要的工具
from sklearn.model_selection import train_test_split # 用於分割資料
from sklearn.linear_model import LinearRegression    # 線性迴歸模型

# 設定中文字型，讓我們等等的圖表能正常顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 我們用 NumPy 來模擬一些房地產數據
# 假設我們有 50 筆資料
np.random.seed(0) # 讓每次產生的隨機數都一樣，方便重現結果
#坪數 = np.random.rand(50, 1) * 30 + 10  # 產生 50 個 10~40 坪的隨機坪數
#房價 = 坪數 * 15 + 200 + np.random.randn(50, 1) * 30 # 假設房價大致是 坪數*15+200，再加上一些隨機雜訊

#動手實驗 (選做)：試著回到第 2 步，修改一下房價的生成公式（例如把 坪數 * 15 改成 坪數 * 25），看看對最後的結果有什麼影響。
坪數 = np.random.rand(50, 1) * 30 + 10  # 產生 50 個 10~40 坪的隨機坪數
房價 = 坪數 * 25 + 200 + np.random.randn(50, 1) * 30 # 假設房價大致是 坪數*25+200，再加上一些隨機雜訊

# 將特徵 X (坪數) 和目標 y (房價) 準備好
# 在機器學習中，習慣上用大寫 X 代表特徵，小寫 y 代表要預測的目標
X = 坪數
y = 房價

# 將資料的 80% 作為訓練集，20% 作為測試集
# random_state=42 是一個常用的數字，確保每次分割的結果都一樣，方便除錯
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. 建立一個線性迴歸模型的「實體」
model = LinearRegression()

# 2. 使用 .fit() 方法，讓模型從「訓練集」中學習
# 這個 fit 的過程，就是在找出那條最適合的直線
print("模型正在訓練中...")
model.fit(X_train, y_train)
print("模型訓練完成！")

# 使用 .predict() 方法，對測試集進行預測
y_pred = model.predict(X_test)

# 畫出真實資料點 (測試集)
plt.scatter(X_test, y_test, color='blue', label='真實價格')

# 畫出模型的預測線
plt.plot(X_test, y_pred, color='red', linewidth=3, label='模型預測線')

# 加上標題和標籤
plt.title('房價預測模型')
plt.xlabel('坪數')
plt.ylabel('房價 (萬)')
plt.legend() # 顯示圖例

# 顯示圖表
plt.show()

# 你覺得紅色的「模型預測線」，有沒有很好地抓住藍色「真實價格」資料點的整體趨勢？
# 有很多點接近綫，有兩個點剛好精確的抓住了，不能說很好的抓住真實價格，但是答案有接近了。

# 有些藍點在紅線上方，有些在下方，這代表什麼？
# 有些坪數對應的房價超出模型預測線或低於模型預測線，但是模型預測線一定是與全部的點取一個最接近的數值所畫的

# 動手實驗 (選做)：試著回到第 2 步，修改一下房價的生成公式（例如把 坪數 * 15 改成 坪數 * 25），看看對最後的結果有什麼影響。
# 更多點觸碰到綫了，而且很多點也開始很接近綫