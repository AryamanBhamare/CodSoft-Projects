print("1 - ADD")
print("2 - SUBSTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")
option = int(input("choose the operation u wanna perform"))
result = 0

if(option in [1,2,3,4]):
    num1 = int(input("Enter first Number"))
    num2 = int(input("Enter second Number"))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2

else:
    print("Invalid Input")

print("The result of the operation is {}".format(result))



