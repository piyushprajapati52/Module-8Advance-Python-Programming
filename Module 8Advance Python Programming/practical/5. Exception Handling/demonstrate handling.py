# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
# input).

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation: +, -, *, /")
    operation = input("Enter operation: ")

    if operation == '+':
        result =  num1 + num2
    elif operation == '-':
        result =  num1 - num2
    elif operation == '*':
        result =  num1 * num2
    elif operation == '/':
        try:
            result =  num1 / num2
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
            result = None
    else:
        print("Invalid operation!")
        result = None

    if result is not None:
        print(f"Result: {result}")


except ValueError:
    print("Please enter valid numeric values.")
