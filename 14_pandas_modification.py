import pandas as pd
#將範例中的商品 DataFrame 建立起來
shopeeData = {
    '產品名稱': ['手機', '電腦', '耳機', '相機'],
    '價格': [20000, 50000, 10000, 100000],
    '庫存數量': [100, 20, 150, 10]
}
shopeeDF = pd.DataFrame(shopeeData)

#新增一個叫做 '折價後價格' 的欄位，它的值是原始 '價格' 欄位打八折（乘以 0.8）。
shopeeDF['折價後價格'] = shopeeDF['價格'] * 0.8
print("--- 新增'總價值'欄位後的 DataFrame ---")


#將包含了新欄位的整個 DataFrame 印出來。
print(shopeeDF)
print("-----------------------------------------------------------------")

#使用 .sort_values()，將 DataFrame 根據 '庫存數量' 來排序，由多到少 (降序)，並將結果印出來。
print(shopeeDF.sort_values(by = '庫存數量',ascending=False))