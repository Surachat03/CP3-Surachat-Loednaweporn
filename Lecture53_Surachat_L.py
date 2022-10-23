def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
totalPrice = int(input("Price:"))
print("Result =",vatCalculate(totalPrice))
