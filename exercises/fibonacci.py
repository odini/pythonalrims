def fib(n):
    a, b = 1, 1
    for i in xrange(n-1):
        a, b = b, a+b
    return a

def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
