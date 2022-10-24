systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45}
menulist = []

def showBill():
    total = 0
    print("----My Food ----")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1],"THB")
        total += int(menulist[number][1])
    print("Total :",total,"THB")
def showmenu():
    print("----------ร้านข้าวมันไก่----------")
    print("------------Menu-------------")
    print(systemMenu)
showmenu()
while True:
    menuName  = input("Please Enter Menu :")
    if (menuName.lower()== "exit"):
        break
    elif menuName != "ข้าวหมกไก่"and menuName != "ข้าวมันไก่" and menuName !="ข้าวมันไก่ผสม" and menuName !="ข้าวมันไก่พิเศษ":
        print("ลูกค้าสั่งเมนูผิดกรุณาสั่งใหม่อีกครั้ง")
    else:
        menulist.append([menuName,systemMenu[menuName]])
showBill()

