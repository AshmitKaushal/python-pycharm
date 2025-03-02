# class variables are the variables which are defined at the class level and shared among all the objects.
# They are defined outside of method and usually store the information that are common for all the objects

class Employee:

    def __init__(self,name,role):
        self.name = name
        self.role = role

    def show(self):
        print(f"The name of the employee is {self.name} and role is {self.role}")


e1 = Employee('GOGO',"Developer")
e1.show()
# It is internally converted into this ClassName.methodName(object)
Employee.show(e1)
print()

print('----------------------Class and Instance Variables------------------------')


class Employee1:

    company = 'Apple'
    EmployeeNo = 0
    def __init__(self,name,raise_amount):
        self.name = name
        self.raise_amount = raise_amount
        Employee1.EmployeeNo +=1
    def show(self):
        print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount} and company name is {self.company}")


e1 = Employee1("GOGO",0.02)
e1.show()
# Here a new instance variable is created not the class variable value change.
# Now the company name for the e1 is changed
e1.company = "Apple India"
e1.show()



e2 = Employee1("Singh",0.3)
e2.show()

print(f"The total number of employees in the {Employee1.company} is {Employee1.EmployeeNo}")