def divide(x, y):
    """Function to perform division."""
    return x / y

def main():
    while True:
        try:
            # Take input from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform division
            result = divide(num1, num2)
            print(f"The result of {num1} divided by {num2} is: {result}")
            break  # Exit the loop if successful

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
