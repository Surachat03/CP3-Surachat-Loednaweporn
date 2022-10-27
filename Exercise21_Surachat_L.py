from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textWeight.get())/math.pow(float(textHight.get())/100,2)
    bmishow = ""
    if float(bmi) >= 30:
        bmishow ="อ้วนมาก"

    elif float(bmi) >=25:
        bmishow ="อ้วน"

    elif float(bmi) >= 23:
        bmishow ="น้ำหนักเกิน"

    elif float(bmi) >= 18.6:
        bmishow ="น้ำหนักปกติ"

    elif float(bmi) <=18.5:
        bmishow ="ผอมเกินไป"

    labelResult.configure(text=bmi)
    labelBmi.configure(text=bmishow)



MainWindow = Tk()

labelHight = Label(MainWindow,text="ส่วนสูง (Cm.)")
labelHight.grid(row=0,column=0)
textHight = Entry(MainWindow)
textHight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textWeight = Entry(MainWindow)
textWeight.grid(row=1,column=1)

button = Button(MainWindow,text = "คำนวณBMI")
button.bind('<Button-1>',leftClickButton)
button.grid(row=2)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

labelBmi = Label(MainWindow,text="BMI")
labelBmi.grid(row=3,column=1)
MainWindow.mainloop()