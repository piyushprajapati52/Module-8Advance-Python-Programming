# Define a custom exception class
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'CustomError: {self.message}'
def check_value(x):
    if x < 0:
        # Raise the custom exception with a message
        raise CustomError("Negative value is not allowed.")
    elif x == 0:
        raise CustomError("Zero is not a valid input.")
    else:
        print(f"Value {x} is valid.")
try:
    value = int(input("Enter a number: "))
    check_value(value)
except CustomError as e:
    print(e)