menulist = []

def showBill():
    total = 0
    print("----My Food ----")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1],"THB")
        total += int(menulist[number][1])
    print("Total :",total,"THB")

while True:
    menuName  = input("Please Enter Menu :")
    if (menuName.lower()== "exit"):
        break
    else:
        menuPrice = input("Price :")
        menulist.append([menuName,menuPrice])
showBill()

