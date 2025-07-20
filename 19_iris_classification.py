# 1. 匯入所有必要的函式庫
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris # <-- 這次的主角

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 2. 載入數據集
print("正在載入鳶尾花數據集...")
iris_dataset = load_iris()

# 讓我們看看這個數據集裡面有什麼
# print(iris_dataset.DESCR) # 你可以取消這行的註解，來看看完整的數據說明

# 3. 轉換為 DataFrame
# iris_dataset.data 是特徵數據，iris_dataset.feature_names 是欄位名稱
df = pd.DataFrame(data=iris_dataset.data, columns=iris_dataset.feature_names)

# 新增一欄 'species'，存放花的品種標籤 (0, 1, 2)
df['species'] = iris_dataset.target

# 為了讓圖表更好看，我們再新增一欄品種的真實名稱
# .map() 可以幫我們做一個對照轉換
df['species_name'] = df['species'].map({0: 'setosa (山鳶尾)', 1: 'versicolor (變色鳶尾)', 2: 'virginica (維吉尼亞鳶尾)'})

# 4. 對 DataFrame 進行「健康檢查」
print("\n--- 資料表頭五筆 ---")
print(df.head())

print("\n--- 資料表詳細資訊 ---")
df.info()

print("\n--- 各品種數量統計 ---")
print(df['species_name'].value_counts())

# 5. 使用 pairplot 進行視覺化探索
print("\n正在繪製關係圖，請稍候...")
# hue='species_name' 讓 pairplot 用不同顏色來區分花的品種
sns.pairplot(df, hue='species_name', markers=["o", "s", "D"])

# 為圖表加上一個總標題
plt.suptitle('鳶尾花數據集特徵關係圖', y=1.02)

# 顯示圖表
plt.show()

# 解讀 pairplot：仔細觀察最後的圖表，然後在心裡回答這個問題：
# 「你認為哪一個特徵（花萼長度/寬度，花瓣長度/寬度）最能夠幫助我們區分出 setosa (山鳶尾) 這個品種？為什麼？」
# 花瓣的長度和寬度，因爲每種花的分佈圖最廣，重叠率低