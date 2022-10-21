usernameInput = input("Usename :")
passwordInput = input("Password :")
if usernameInput == "Hajime" and passwordInput == "Fury":
    print("เข้าสู่ระบบ")
    print("-------Welcome------")
    print("-----HajimeShop-----")
    print("Iphone 20000บาท/เครื่อง")
    print("Charger 790บาท/ชิ้น")
    print("Powerbank 2250บาท/ชิ้น")
    print("Case 250บาท/ชิ้น")
    print("Airpod 7500บาท/ชิ้น")
    print("ProtectiveFlim 300บาท/ชิ้น")
    Iphone = 20000
    Charger = 790
    Powerbank = 2250
    Case = 250
    Airpod = 7500
    ProtectiveFlim = 300
    Vat = 7
    Product = input("สินค้าที่ต้องการซื้อ : ")
    Amount = int(input("จำนวนที่ต้องการซื้อ :"))
    if Product == "Iphone":
        print("Price","รวมภาษีมูลค่าเพิ่ม :",(Iphone*Amount)+(Iphone*Amount)*Vat/100,"THB")
    elif Product == "Charger":
        print("Price", "รวมภาษีมูลค่าเพิ่ม :", (Charger * Amount) + (Charger * Amount) * Vat / 100, "THB")
    elif Product == "Powerbank":
        print("Price", "รวมภาษีมูลค่าเพิ่ม :", (Powerbank * Amount) + (Powerbank * Amount) * Vat / 100, "THB")
    elif Product == "Case":
        print("Price", "รวมภาษีมูลค่าเพิ่ม :", (Case * Amount) + (Case * Amount) * Vat / 100, "THB")
    elif Product == "Airpod":
        print("Price", "รวมภาษีมูลค่าเพิ่ม :", (Airpod * Amount) + (Airpod * Amount) * Vat / 100, "THB")
    elif Product == "ProtectiveFlim":
        print("Price", "รวมภาษีมูลค่าเพิ่ม :", (ProtectiveFlim * Amount) + (ProtectiveFlim * Amount) * Vat / 100, "THB")
    elif Product =="Iphone" or "Charger" or "Powerbank" or "Case" or "Airpod" or "ProtectiveFlim":
        print("ข้อมูลสั่งซื้อผิดพลาด กรุณาลองใหม่อีกครั้ง")
    print("-----Thank you-----")
else:
    print("Username หรือ Password ไม่ถูกต้องกรุณาลองใหม่อีกครั้ง")


