# When the subclass define the method that is already defined in the parent class then the method is knows method overriding
# But the method must be defined with same number of parameters


class A:

    def show(self):
        print("Hello from class A")

class B:

    def show(self):
        print("Hello from class B")


a1 = A()
a1.show()
b1 = B()
b1.show()