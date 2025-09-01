# 4. Hierarchical Inheritance
# Hierarchical Inheritance: One parent → Multiple children

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def child1_method(self):
        print("This is Child 1")

class Child2(Parent):
    def child2_method(self):
        print("This is Child 2")

obj1 = Child1()
obj2 = Child2()

obj1.greet()
obj1.child1_method()

obj2.greet()
obj2.child2_method()