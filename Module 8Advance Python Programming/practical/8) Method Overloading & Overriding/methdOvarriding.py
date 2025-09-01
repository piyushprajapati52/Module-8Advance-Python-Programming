#  Write a Python program to show method overriding.

class Animal:
    def sound(self):
        print("The animal makes a sound")
    
class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()
