# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_fast(a, b):
    while(b):
        a, b = b, a%b
    return a    
    
def lcm_fast(a, b):
    return a*b // gcd_fast(a, b)
    
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))
    '''
    a, b = 6, 8
    print(lcm_naive(a, b), lcm_fast(a, b))
    '''