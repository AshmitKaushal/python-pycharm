# Multi level Inheritance

# When a child class act as a parent class for another child class, it is called multi-level inheritance.

class A:

    def show(self):
        print("Hello from class A")

class B(A):

    def display(self):
        print("Hello from class B")

class C(B):

    def details(self):
        print("Hello from class C")

c1 = C()
c1.show()