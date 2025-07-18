# 建立一個空的購物清單 (空的置物櫃)
shopping_list = []

# 使用 input() 函式，提示使用者輸入第一樣想買的商品，並用 .append() 將其加入 shopping_list。
shopping_list.append(input("請輸入您第一樣想購買的商品: "))


# 再次使用 input() 函式，提示使用者輸入第二樣想買的商品，並用 .append() 將其加入 shopping_list。
shopping_list.append(input("請輸入您第二樣想購買的商品: "))

# 最後，使用 print() 函式，印出類似「你的購物清單是：[...]」的訊息，並顯示整個 shopping_list。
print("你的購物清單是：",shopping_list)

# 挑戰題： 在印出清單後，再用 len() 函式印出「清單上總共有 ... 樣商品。」
print("清單上總共有", len(shopping_list), "樣商品。")