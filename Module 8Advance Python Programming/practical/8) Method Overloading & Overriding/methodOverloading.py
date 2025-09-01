# Write a Python program to show method overloading

class Calculator:
    def multiply(self,*args):
        result = 1
        if not args:
            return 0
        for num in args:
            result *= num
        return result

calc = Calculator()

print(calc.multiply())
print(calc.multiply(5))
print(calc.multiply(2,3))