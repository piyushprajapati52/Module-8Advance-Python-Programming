# 5. Hybrid Inheritance

class A:
    def method_a(self):
        print("Class A method")

class B(A):
    def method_b(self):
        print("Class B method")

class C(A):
    def method_c(self):
        print("Class C method")

class D(B, C):
    def method_d(self):
        print("Class D method")

obj = D()
obj.method_a()  
obj.method_b()  
obj.method_c()  
obj.method_d()  