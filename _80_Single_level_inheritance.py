# When the class inherits all the attributes and properites of the other class is knows as inheritance

class A:

    def show(self):
        print("THis is class A")

class B(A):

    def display(self):
        print("This is class B")

a1 = A()
a1.show()
b1 = B()
b1.show()
b1.display()