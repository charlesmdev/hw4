def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def numOfWays(n):
    if 1 <= n <= 25:
        return fib(n + 1)

