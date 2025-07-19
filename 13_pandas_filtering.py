import pandas as pd
shopeeData = {
    '產品名稱': ['手機', '電腦', '耳機','相機'],
    '價格': [20000,50000,8000,100000],
    '庫存數量': [100, 20, 150,10]
}
shopeeDF = pd.DataFrame(shopeeData)

# 選取出所有 '價格' 小於 60000 的商品
print("選取出所有 '價格' 小於 60000 的商品:\n",shopeeDF[shopeeDF['價格']<60000])

#選取出所有 '庫存數量' 大於 50 的商品。
print("選取出所有 '庫存數量' 大於 50 的商品:\n",shopeeDF[shopeeDF['庫存數量']>50])

#選取出 '產品名稱' 等於 '電腦' 的那筆資料 (提示: df['產品名稱'] == '電腦')。
print("選取出 '產品名稱' 等於 '電腦' 的那筆資料:\n",shopeeDF[shopeeDF['產品名稱'] == '電腦'])

#挑戰題：選取出 '價格' 大於 15000 而且 (&) '庫存數量' 小於 150 的商品。
print("選取出 '價格' 大於 15000 而且 (&) '庫存數量' 小於 150 的商品:\n",shopeeDF[(shopeeDF['價格'] > 15000 )&(shopeeDF['庫存數量']<150)])

'''''
# 建立一個條件：價格是否大於 30000?
condition = df['價格'] > 30000
print("--- 條件 (布林遮罩) ---")
print(condition)

# 把遮罩放進 DataFrame
high_price_products = df[condition]
print("\n--- 價格昂貴的商品 ---")
print(high_price_products)

high_price_products = df[df['價格'] > 30000]
print("\n--- (一行完成) 價格昂貴的商品 ---")
print(high_price_products)

# 找出「價格 > 15000」 而且 「庫存 < 50」的商品
# (df['價格'] > 15000) & (df['庫存數量'] < 50)
best_deals = df[(df['價格'] > 15000) & (df['庫存數量'] < 50)]

print("\n--- 高價且稀有的商品 ---")
print(best_deals)
'''