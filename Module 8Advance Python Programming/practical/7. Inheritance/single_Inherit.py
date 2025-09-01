#  Single Inheritance

class parent:
    def greet(self):
        print("Hello, I am parent class")

class child(parent):
    def say(self):
        print("Hello, I am child class")

obj = child()
obj.greet()
obj.say()