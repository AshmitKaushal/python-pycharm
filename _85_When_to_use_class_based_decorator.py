# When to Use Class-Based Decorators
# When You Need to Maintain State:
# If your decorator needs to track information across multiple calls or manage data, a class is ideal.
# Example: Counting the number of times a function is called.

class Counter:

    def __init__(self,func):
        self.func = func
        self.count = 0

    def __call__(self,*args):
        self.count+=1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args)

@Counter
def greet(name):
    print(f"Hello {name}")

greet("ALice")
greet('GOGO')


class Logger:

    def __init__(self,func):
        self.func = func

    def log_before(self,*args):
        print(f"Before call argument is {args}")

    def log_after(self,result):
        print(f"After call arugment is {result}")

    def __call__(self,*args):
        self.log_before(*args)
        result = self.func(*args)
        self.log_after(result)
        return result

@Logger
def add(a,b):
    return a+b

add(10,20)