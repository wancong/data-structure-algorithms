# Uses python3
import sys

def get_majority_element(a, left, right):
    m, count = 0, 1
    for i in range(1, right):
        #print('i->',i,' m->',m,' count->',count)
        if a[i] == a[m]:
            count += 1
        else:
            count -= 1
        if count == 0:
            m, count = i, 1
    count = 0
    for i in range(right):
        if a[i] == a[m]:
            count += 1
    if count > right / 2:
        return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
