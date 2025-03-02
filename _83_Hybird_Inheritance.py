# Hybrid Inheritance

# This interitance is the combination of the multiple inheritance and hiearchical inheritance

class A:

    def show(self):
        print("HEllo from class A")

class B(A):

    def display(self):
        print("Hello from class B")

class C(A):

    def details(self):
        print("Hello from class C")

class D(B,C):

    def info(self):
        print("Hello from class D")

d1 = D()
d1.info()