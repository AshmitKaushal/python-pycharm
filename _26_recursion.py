# when a function calls itself is know as recursion.

def seq(n):
    if n==0:
        return
    print(n)
    n = n - 1
    return seq(n)

seq(5)