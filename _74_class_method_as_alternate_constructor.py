# class method used to create factory methods

'''
A factory method in Python is a design pattern used to create objects in a structured and standardized way.
It is typically implemented using class methods to provide an alternative constructor for a class.
The factory method allows the creation of objects in various formats
or from diverse inputs without requiring the caller to know the exact details of the object construction process.
'''

'''
Why we are using class method suppose we are creating the object but the data always does not come in valid format
ex come in string format like that 'GOGO-12000'
but the constructor contains name and salary as separate with the help of class method we can create instance of the class
as class method first parameter is cls which the class itself on writing cls() a constructor is called and constructor are used to initialize the instance of the class.

'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

    @classmethod
    def form_String(cls,data):
        print("This is the class method and name of the class is",cls)
#         Here the constructor is called on writing cls() which class name()
#         Whenever we write class name() the constructor is invoked which is the __init__ which create the instance of the class.
        name,salary = data.split('-')[0],data.split('-')[1]
        return cls(name,int(salary))

# Employee.form_String()
e1 = Employee('GOGO',12000)
e1.show()

# Now the data comes in string format so we will be using class method as the alternate constructor.
data = "Singh-15000"
e2 = Employee.form_String(data)
e2.show()

