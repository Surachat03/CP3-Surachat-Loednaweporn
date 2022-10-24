menulist = []
pricelist = []
def showBill():
    total = 0
    print("----My Food ----")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number],"THB")
        total += int(pricelist[number])  #+= คือการเอาค่าที่ต้องการมา+เพิ่มไปเรื่อยๆจนครบลูป
    print("Total :",total,"THB")
while True:
    menuName  = input("Please Enter Menu :")
    if (menuName.lower()== "exit"):
        break
    else:
        menuPrice = input("Price :")
        menulist.append(menuName)
        pricelist.append(menuPrice)
showBill()

