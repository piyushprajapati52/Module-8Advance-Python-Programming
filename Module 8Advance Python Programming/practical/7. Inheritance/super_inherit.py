# Write a Python program to demonstrate the use of
# super() in inheritance.

class Parent:
    def __init__(self,name):
        self.name = name

    def display_info(self):
        print("Name is:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}\nage: {self.age}")


obj = Child("Piyush",22)

obj.display_info()  
