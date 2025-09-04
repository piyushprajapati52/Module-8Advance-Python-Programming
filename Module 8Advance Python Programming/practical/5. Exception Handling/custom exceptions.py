# Write a Python program to print custom exceptions

try:
    num = int(input("Enter a positive number: "))
    if num < 0:

        # Raising a built-in ValueError but with our custom message
        raise ValueError("Negative numbers are not allowed!")
    print(f"You entered: {num}")

except ValueError as e:
    print(f"Custom Exception: {e}")
