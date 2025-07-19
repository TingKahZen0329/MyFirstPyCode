import pandas as pd
# 字典需包含以下三個鍵：'產品名稱' (字串)、'價格' (數值)、'庫存數量' (數值)
shopeeData = {
    #請至少新增 3 到 4 樣商品
    '產品名稱': ['手機', '電腦', '耳機','相機'],
    '價格': [20000,50000,8000,100000],
    '庫存數量': [100, 20, 150,10]
}

# 將你建立的 DataFrame 印出來
shopeeDF = pd.DataFrame(shopeeData)
print(shopeeDF)

# 使用 .head() 查看前幾筆資料
print("--- .head() ---")
print(shopeeDF.head())

#使用 .info() 查看詳細資訊
print("\n--- .info() ---")
shopeeDF.info()

#使用 .describe() 查看統計數據
print("\n--- .describe() ---")
print(shopeeDF.describe())