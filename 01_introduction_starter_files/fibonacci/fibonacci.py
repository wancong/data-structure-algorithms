# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    if (n <= 1):
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b
    
n = int(input())
#print(calc_fib(n))
print(calc_fib_fast(n))
#for n in range(20):
#    print(calc_fib(n), calc_fib_fast(n))
