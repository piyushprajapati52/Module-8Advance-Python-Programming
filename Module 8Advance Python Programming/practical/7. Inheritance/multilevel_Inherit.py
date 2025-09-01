# 3. Multilevel Inheritance

class Grandparent:
    def greet_gp(self):
        print("Hello from Grandparent.")

class parent(Grandparent):
    def greet_p(self):
        print("Hello from Parent.")

class child(parent):
    def greet_c(self):
        print("Hello from child.")

obj = child()

obj.greet_gp()
obj.greet_p()
obj.greet_c()