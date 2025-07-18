import random
# 來產生一個 1 到 100 之間的隨機整數，作為這次遊戲的答案
secret_number = random.randint(1, 100)

'''判斷輸贏：

如果 使用者猜的數字 等於 secret_number：

印出「恭喜你猜對了！」

使用 break 來跳出無窮迴圈，結束遊戲。

否則如果 (elif) 使用者猜的數字 小於 secret_number：

印出「太小了，再猜大一點！」

否則 (else)：

印出「太大了，再猜小一點！」

在迴圈結束後 (也就是 break 之後)，可以印出一句「遊戲結束，歡迎下次再來！」。'''
while True:
    num = int(input("請輸入一個1-100的數字，來看一下和我的答案會不會一樣: "))
    if num == secret_number:
        print("恭喜你，答對了！")
        break
    elif num < secret_number:
        print("太小了，再猜大一點！")
    else:
        print("太大了，再猜小一點！")
print("遊戲結束，歡迎下次再來！")