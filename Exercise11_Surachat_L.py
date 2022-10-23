number = int(input("Please select your number >>> "))
text = "*"
print(" " * number, text)
for x in range(number):
    for y in range(2):
        text += "*"
    if text == "***********":
            break
    print(" " * (number - (x + 1)), text)