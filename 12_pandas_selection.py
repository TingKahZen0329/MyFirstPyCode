import pandas as pd
shopeeData = {
    '產品名稱': ['手機', '電腦', '耳機','相機'],
    '價格': [20000,50000,8000,100000],
    '庫存數量': [100, 20, 150,10]
}
shopeeDF = pd.DataFrame(shopeeData)

# 只選取 '價格' 這一欄，並印出來
priceShopee = shopeeDF['價格']
print("---只選取 '價格' 這一欄---")
print(priceShopee)
print("--------------------------")

#同時選取 '產品名稱' 和 '庫存數量' 這兩欄，並印出來
productAndStockQuaOfShopee = shopeeDF[['產品名稱','庫存數量']]
print("---同時選取 '產品名稱' 和 '庫存數量' 這兩欄---")
print(productAndStockQuaOfShopee)
print("--------------------------")

#使用 .loc 選取第二筆商品的所有資料 (列標籤為 1 的那一行)，並印出來
computerInformation = shopeeDF.loc[1]
print("---電腦的所有資料---")
print(computerInformation)
print("--------------------------")

#挑戰題：使用 .loc 選取第一筆商品 (列標籤為 0) 的 '價格'，並印出來
phonePrice = shopeeDF.loc[0,'價格']
print("---手機的價格為: ",phonePrice)