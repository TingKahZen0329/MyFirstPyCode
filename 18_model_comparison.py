# 1. 匯入所有必要的函式庫
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor # <-- 我們的新挑戰者！
from sklearn.metrics import mean_squared_error

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 2. 準備和分割資料 (和上次完全一樣，確保公平比較)
np.random.seed(0)
坪數 = np.random.rand(50, 1) * 30 + 10
房價 = 坪數 * 15 + 200 + np.random.randn(50, 1) * 30
X = 坪數
y = 房價.ravel() # .ravel() 將 y 轉為一維陣列，這是 fit 方法更喜歡的格式

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 模型一：線性迴歸 (複習) ---
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
# 取得斜率 m (因為 X 可能是多維的，所以它被存在 .coef_ 這個屬性裡)
slope_m = lr_model.coef_[0]

# 取得截距 b
intercept_b = lr_model.intercept_

print(f"\n模型學到的公式:")
print(f"斜率 (m): {slope_m:.2f}")
print(f"截距 (b): {intercept_b:.2f}")
print(f"所以，模型的預測公式是： 房價 = {slope_m:.2f} * 坪數 + {intercept_b:.2f}")

# --- 模型二：隨機森林 (新挑戰者) ---
# n_estimators=100 代表這個森林裡有 100 棵樹
# random_state=42 確保森林的「隨機性」是可重現的
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# --- 4. 比較結果 ---
print("--- 模型表現評估 (RMSE) ---")
print(f"線性迴歸 (Linear Regression) 的 RMSE: {rmse_lr:.2f}")
print(f"隨機森林 (Random Forest) 的 RMSE:   {rmse_rf:.2f}")

if rmse_rf < rmse_lr:
    print("\n贏家是：隨機森林！")
else:
    print("\n贏家是：線性迴歸！")

# --- 5. 視覺化比較 ---
# 為了讓折線圖正確連接，我們先對 X_test 進行排序
sort_axis = X_test.flatten().argsort()
X_test_sorted = X_test[sort_axis]
y_pred_lr_sorted = y_pred_lr[sort_axis]
y_pred_rf_sorted = y_pred_rf[sort_axis]

plt.scatter(X_test, y_test, color='blue', label='真實價格')
plt.plot(X_test_sorted, y_pred_lr_sorted, color='red', linewidth=3, label='線性迴歸預測線')
plt.plot(X_test_sorted, y_pred_rf_sorted, color='green', linewidth=3, linestyle='--', label='隨機森林預測線')

plt.title('線性迴歸 vs. 隨機森林')
plt.xlabel('坪數')
plt.ylabel('房價 (萬)')
plt.legend()
plt.show()

# 觀察結果：看看終端機印出來的 RMSE 數值，哪一個模型更低？
# 綫性回歸（22.38） 隨機森林（35.20）

# 解讀圖表：看看最後的圖表，綠色的虛線（隨機森林）和紅色的實線（線性迴歸）有什麼不同？你覺得哪一條線更「貼近」藍色的真實資料點？
# Kah Zen: 照理上，隨機森林應該會取勝，但是因爲我們給他的種子不太夠，所以雖然他很努力的再往點靠攏，但還是有碰到點的綫并沒有綫性回歸更接近（也就是均平方值沒有很低）
# Kah Zen: 第一次的想法是錯誤的因爲隨機森林他太專業了，導致過擬合導致的，什麽都抓
#          線性迴歸 (一個數學家)：他看到這些數據後，說：「我知道這些數據有些波動，但我認為最核心的規律就是一條直線。」他給出了一個簡潔、抓住大方向的答案
#          隨機森林 (100 個過度認真的專家)：
#           委員會裡的第一個專家（第一棵樹）看到數據，他不僅看到了「坪數越大、房價越高」的趨勢，他還特別記住了：「哦，在 23 坪的時候，房價好像稍微高了一點點，我得把這個細節記下來。」
#           第二個專家（第二棵樹）也記住了這個趨勢，但他可能又對另一個雜訊點產生了印象：「在 35 坪時，房價好像又偏低了一點，這一定是個重要規則！」
#           ...以此類推，100 個專家，每一個都試圖完美地解釋他在訓練資料中看到的每一個微小的波動。
#           結果就是： 這個由 100 個過度擬合的專家組成的委員會，雖然對「課本和習題」（訓練集）的內容倒背如流，
#                     但他們學到的知識裡，包含了太多「雜訊」和「巧合」。當面對他們沒見過的「模擬考題」（測試集）時，
#                     這些被當成知識的「雜訊」反而成了干擾，導致整體預測的誤差變大。
#          結論：隨機森林 會在以下情況中，輕鬆擊敗線性迴歸：
#          非線性關係：當「坪數」和「房價」的關係不是一條直線時。例如，房價可能在坪數超過 50 坪後，
#                     上漲速度變慢。線性迴歸無法捕捉這種「轉折」，但隨機森林可以。

#          多個特徵：當我們不只有「坪數」一個特徵，還加入了「屋齡」、「離捷運站距離」、「房間數量」等數十個特徵時。
#                   隨機森林非常擅長處理這種多維度的複雜問題，而簡單的線性迴歸可能就難以應付了。
#          Entities should not be multiplied without necessity.
#          如果簡單的方法可以解決（綫性回歸），就沒有必要用複雜的方式解決（隨機森林），除非問題本身就很複雜，不能用簡單的方法來解決