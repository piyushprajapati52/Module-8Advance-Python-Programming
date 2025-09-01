# Define a class named Person
class Person:
    def __init__(self, name, age):
        self.name = name  # Property: name
        self.age = age    # Property: age
# Create an object of the Person class
person1 = Person("Alice", 30)
# Access and print the properties using the object
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")