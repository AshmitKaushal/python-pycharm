print("Do-While Using while loop")
i = 1
while(True):
    print(i)
    i = i + 1
    if i==10:
        break


print("Do-While using for loop")
i = 1
for _ in iter(int,1):
    print(i)
    if i==10:
        break
    i = i + 1

'''
    
How iter(int, 1) Works
int as a Callable:

The first argument to iter() is a callable, which is a function or method that can be called without arguments. Here, int is a callable object.
Every time the iterator calls int(), it always returns 0 (since calling int() without arguments defaults to 0).
1 as a Sentinel Value:

The second argument is the sentinel value. The iterator stops when the callable returns this sentinel value.
In this case, the sentinel is 1, which int() never returns (since int() always returns 0 when called without arguments).
Infinite Loop Behavior:

Since int() keeps returning 0, which is not equal to the sentinel value 1, the loop never terminates by itself. It runs indefinitely unless explicitly stopped using a break.
Why Use iter(int, 1)?
This construct creates an infinite iterator because:

The callable int keeps returning 0.
The iterator never reaches the sentinel value 1.
This trick is commonly used to simulate an infinite loop while still adhering to Python's iterator protocol.

Detailed Execution of the Code
Initialization:

iter(int, 1) creates an infinite iterator.
for Loop:

The loop body is executed repeatedly because the iterator never reaches the sentinel value 1.
Incrementing count:

The count variable is incremented in each iteration.
Exit Condition:

When count reaches 5, the loop breaks using the break statement.
Why Not Use a while True Loop Instead?
You could replace this iter(int, 1) construct with a while True loop:

python
Copy code
count = 0
while True:
    print(f"Current count: {count}")
    count += 1
    if count >= 5:
        print("Count reached 5. Breaking out of the loop.")
        break
However, the iter(int, 1) trick is sometimes preferred because:

It uses Python's iterator protocol, which can make it more readable or idiomatic in certain contexts.
It is an example of leveraging Python's built-in tools for creative control over looping behavior.
Let me know if you'd like further clarification!'''