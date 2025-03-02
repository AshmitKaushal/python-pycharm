# Operator Overloading in method is refers to the ability of modifying the behaviour of the operator such as (+,-,/) etc for the user defined object.

class Vector:

    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

    def __add__(self,other):
        return Vector(self.i+other.i,self.j+other.j,self.k+other.k)


v1 = Vector(3,4,5)
v1.show()

v2 = Vector(4,5,6)
v2.show()

# We want the addition of the vector object which is not responsible we can't perform + on user defined object
# So we will be using special methods dunder to modify the behaviour of the + operator
# On using + __add__ method defined in the class is called.
# in which v1 and v2 are automatically passed as an arugment.

v3 = v1 + v2
# it is internally called like that v1.__add__(v2)
v3.show()
v4 = v1.__add__(v2)
v4.show()