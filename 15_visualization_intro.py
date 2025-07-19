# 匯入必要的函式庫
# matplotlib.pyplot 簡稱為 plt
import matplotlib.pyplot as plt
# 準備資料：自己定義兩組 list 資料。例如，模擬過去六個月的銷售額：
print("正在準備繪圖資料...")
months = [1, 2, 3, 4, 5, 6]
sales = [52, 65, 88, 79, 95, 110]

# 繪製圖表：使用 plt.plot() 將這兩組資料畫成折線圖。
print("正在繪製圖表...")
plt.plot(months, sales)

# 客製化圖表：為你的圖表加上一個有意義的標題 (例如"Sales Trend Over 6 Months")，以及 X 軸和 Y 軸的標籤。
plt.title("Sales Trend Over 6 Months")      # 加上圖表標題
plt.xlabel("Months")           # 加上 X 軸的標籤
plt.ylabel("Sales")   # 加上 Y 軸的標籤

# 顯示圖表：使用 plt.show()展示出來！
print("即將顯示圖表... (請在跳出的視窗中查看，關閉視窗後程式才會繼續)")
plt.show()
print("圖表視窗已關閉，程式執行結束。")