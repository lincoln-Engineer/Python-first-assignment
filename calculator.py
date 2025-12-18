# Basic Calculator Program

# Here i am getting the two numbers and the operation from the user

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Here I am performing calculation

#operation for addition
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

#operation for subtraction
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

#operation for multiplication
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

#operation for division
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation! Please use +, -, *, or /.")
