# 1. 匯入所有需要的函式庫
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # 我們仍然需要它來顯示圖表

# --- 解決中文顯示問題的魔法程式碼 ---
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
# -----------------------------------
# 2. 用 Pandas DataFrame 來準備資料 (這是專業的做法)
product_data = {
    '產品名稱': ['手機', '電腦', '耳機', '相機'],
    '價格': [20000, 50000, 10000, 100000]
}
df_products = pd.DataFrame(product_data)

# 使用 sns.barplot()，將每種 '產品名稱' 和它對應的 '價格' 畫成長條圖
# （提示：x 軸是 '產品名稱'，y 軸是 '價格'）
print("正在使用 Seaborn 繪製圖表...")
sns.barplot(data=product_data, x='產品名稱', y='價格')

# 為圖表加上標題，例如「各產品價格比較」
plt.title("各產品價格比較")

# 5. 顯示圖表
plt.show()