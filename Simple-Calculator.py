def addition(x , y):
    return x + y
def subtraction(x , y):
    return x - y
def multiplication(x , y):
    return x * y
def division(x , y):
    if y == 0:
        return "Cannot be divisible by 0"
    else:
        return x / y
while True:
    print("********** SIMPLE CALCULATOR **********")
    print("List of Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your Choice: ")
    if choice == '5':
        print("Existing the Calculator")
        break
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    if choice == '1':
        print("Result: " , addition(num1 , num2))
    elif choice == '2':
        print("Result: " , subtraction(num1 , num2))
    elif choice == '3':
        print("Result: " , multiplication(num1 , num2))
    elif choice == '4':
        print("Result: " , division(num1 , num2))
    else:
        print("Invalid Input")





