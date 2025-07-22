# 1. 匯入所有必要的函式庫
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 匯入我們今天所有的參賽選手！
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC # 支持向量機 (Support Vector Classifier)
from sklearn.tree import DecisionTreeClassifier

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 2. 載入並準備資料 (和上次完全一樣)
iris_dataset = load_iris()
X = iris_dataset.data
y = iris_dataset.target

# 3. 分割訓練集和測試集 (和上次完全一樣，確保公平)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. 建立我們的參賽選手名單
# 我們用一個字典來存放模型，方便管理
models = {
    "K-鄰近演算法 (KNN)": KNeighborsClassifier(n_neighbors=5),
    "邏輯斯迴歸 (Logistic Regression)": LogisticRegression(max_iter=200),
    "支持向量機 (SVM)": SVC(),
    "決策樹 (Decision Tree)": DecisionTreeClassifier(random_state=42)
}

# 5. 讓選手一一上場比賽
print("--- AI 模型武鬥大會開始！ ---")

# 用一個字典來儲存每個模型的成績
results = {}

for model_name, model in models.items():
    # 訓練模型
    model.fit(X_train, y_train)
    
    # 進行預測
    y_pred = model.predict(X_test)
    
    # 計算準確率
    accuracy = accuracy_score(y_test, y_pred)
    
    # 將結果記錄下來
    results[model_name] = accuracy
    
    print(f"\n選手: {model_name}")
    print(f"準確率: {accuracy:.2%}")

# 6. 公布最終比賽結果
print("\n\n--- 最終比賽結果 ---")
# 我們可以對 results 字典進行排序，找出冠軍
# key=results.get 代表根據字典的「值」(也就是準確率) 來排序
# reverse=True 代表由高到低排
sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)

for i, (model_name, accuracy) in enumerate(sorted_results):
    if i == 0:
        print(f"🏆 冠軍: {model_name} (準確率: {accuracy:.2%})")
    else:
        print(f"   第 {i+1} 名: {model_name} (準確率: {accuracy:.2%})")


#  看看終端機印出來的最終排名。誰是這次的冠軍？
#  并沒有誰是冠軍吧，大家準確率都一樣

#  你會發現，這次所有模型的準確率都非常高，甚至都是 100%。這再次證明了鳶尾花數據集是一個特徵非常清晰、相對簡單的問題

#  在真實世界的複雜問題中，不同模型的表現差異會非常巨大，而我們今天的這套「比較流程」，就是未來挑選最佳模型的核心方法。