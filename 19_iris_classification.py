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
# --- 新增這一段，先把欄位名改成中文 ---
chinese_column_names = ['花萼長度(cm)', '花萼寬度(cm)', '花瓣長度(cm)', '花瓣寬度(cm)']
df.columns = chinese_column_names + ['species', 'species_name'] # 注意要包含後面兩欄
# ------------------------------------

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

# (你之前的 EDA 程式碼都保留)

# --- 接下來是模型訓練的部分 ---

# 6. 準備特徵 (X) 和目標 (y)
# X 是我們用來預測的特徵 (花萼長寬、花瓣長寬)
X = df[['花萼長度(cm)', '花萼寬度(cm)', '花瓣長度(cm)', '花瓣寬度(cm)']]
# y 是我們要預測的目標 (花的品種)
y = df['species_name']

# 7. 分割訓練集和測試集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 8. 匯入、建立並訓練 KNN 模型
from sklearn.neighbors import KNeighborsClassifier

# 建立模型，我們讓它看最近的 5 個鄰居
model = KNeighborsClassifier(n_neighbors=5)

print("\n--- 模型正在訓練中... ---")
model.fit(X_train, y_train)
print("--- 模型訓練完成！ ---")

# 9. 進行預測
y_pred = model.predict(X_test)

# 10. 評估模型表現
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"\n模型在測試集上的準確率 (Accuracy): {accuracy:.2%}") # .2% 會將數字格式化為百分比
# 觀察結果：看看最後印出來的「準確率」有多高？這個數字代表在模型從沒見過的測試集數據中，它答對了百分之多少的題目
# 模型在測試集上的準確率 (Accuracy): 100.00%