def calculate(operation, x, y):
    """Function to perform basic arithmetic operations."""
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y
    else:
        raise ValueError("Invalid operation. Please choose add, subtract, multiply, or divide.")

def main():
    while True:
        try:
            # Take input from the user
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip()
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the calculation
            result = calculate(operation, num1, num2)
            print(f"The result of {operation}ing {num1} and {num2} is: {result}")
            break  # Exit the loop if successful

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
