def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else :
        print("รหัสผิดพลาดกรุณาลองใหม่อีกครั้ง")
        login()
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    while userSelected !=1 and userSelected != 2:
        print("กรุณาทำรายการอีกครั้ง")
        menuSelect()
    if userSelected == 1:
        print("ราคาสินค้ารวม vat 7%:",vatCalculate(priceCalculate()),"บาท")
    elif userSelected ==2:
        print("รวมราคาสินค้า",priceCalculate(),"บาท")

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total = price1+price2
    return total
login()
showMenu()
menuSelect()
print("ขอบคุณที่ใช้บริการ")
