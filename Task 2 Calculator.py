def calculator():
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    operator = input("Enter an operator: ")


    if operator == "+":
        num3 = num1 + num2
        print(f"\nThe result is: {num3}")
    elif operator == "-":
        num3 = num1 - num2
        print(f"\nThe result is: {num3}")
    elif operator == "/":
        num3 = num1 / num2
        print(f"\nThe result is: {num3}")
    elif operator == "*":
        num3 = num1 * num2
        print(f"\nThe result is: {num3}")
    else:
        print("Invalid operator or Number!")


quit = ""

while quit == ""or quit == "y":
    calculator()
    quit = input("would you like to continue using calculator (y/n): ").lower()
