# 在程式最上方，建立一個空的串列，當作我們的電話簿：phone_book = []。
phone_book = []

'''
定義一個 add_contact 函式：

這個函式需要三個參數：name, phone, email。

在函式內部，建立一個聯絡人字典，例如：contact = {"name": name, "phone": phone, "email": email}。

使用 .append() 將這個字典新增到全域的 phone_book 串列中。
'''
def add_contact(name,phone,email):
    contact = {"name": name, "phone": phone, "email": email}
    phone_book.append(contact)

'''
定義一個 display_all_contacts 函式：

這個函式不需要參數。

在函式內部，使用 for 迴圈來遍歷 phone_book 串列。

在迴圈中，將每一個聯絡人（也就是每一個字典）的資料都格式化印出來。
'''

def display_all_contacts():
    print("電話簿的内容：")
    for phoneNumber in phone_book:
        print(phoneNumber)

'''
在主程式區塊呼叫函式：

呼叫 add_contact() 兩到三次，新增幾個不同的聯絡人。

呼叫 display_all_contacts() 來顯示你電話簿裡的所有內容。
'''
while True :
    Judge = input("請問您要新增聯絡人嗎？(Y/Other Press) Y = 是，任意鍵直接跳出程序")
    if Judge == "Y":
        name = input("請輸入姓名：")
        phone = input("請輸入電話號碼：")
        email = input("請輸入電子郵件：")
        add_contact(name,phone,email)
    else :
        print("跳出程式！")
        break
display_all_contacts()
