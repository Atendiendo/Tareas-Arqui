def Lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (Lucas(n-1) + Lucas(n-2))
    
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))
    
def aureo(n):
    x = (Lucas(n) + Fibonacci(n)*(5**(1/2)))/2
    return x

print(Lucas(0))