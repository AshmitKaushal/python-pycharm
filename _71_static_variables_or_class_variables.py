# In python there is no static keyword to define the static variable
# Here the variables which are defined outside the method and inside the class are static method and also termed as class variables
# As they are defined at the class level

# These variables are independent of the instance of the class
# and shared among all the instance of the class.
# It is used to store the information that are common for all the objects.

class Employee:
    company = 'XYZ'

    def __init__(self,name,role):
        self.name = name
        self.role = role

    def show(self):
        print(f"the name of the employee is {self.name} and role is {self.role}")

e1 = Employee('GOGO','Developer')
e1.show()

# Class variables are accessed with the class name and instance
print("------------Accessing the class variable using Class name----------")
print(Employee.company)

print("------------Accessing the class variable using instance name----------")
print(e1.company)

# if the name of the instance variable is same as class variable then in that case the value of the instance variable will be printed.


class Student:
    sch = 'XYZ'

    def __init__(self,name,role):
        self.name = name
        self.role = role

    def show(self):
        print(f"the details are {self.name},{self.role},{self.sch}")


s1 = Student('John','Developer')
# Here a new instance variable is created and its value is DDD
s1.sch = 'DDD'
s1.show()

# For the other object the value of the name is still XYZ
s2 = Student('GOGO','Developer')
s2.show()
