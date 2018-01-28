# Uses python3
import sys

def get_change(m):
    #write your code here
    a=b=sum=0
    a, b = m//10, m%10
    sum += a
    a, b = b//5, b%5
    sum += a + b
    return sum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
