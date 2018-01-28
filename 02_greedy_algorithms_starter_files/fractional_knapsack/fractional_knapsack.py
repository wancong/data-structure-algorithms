# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    k = []
    for i in range(len(values)):
        k.append(values[i] / weights[i])
    for _ in range(len(k)):
        max_i = k.index(max(k))
        if capacity <= 0:
            break
        if capacity < weights[max_i]:
            value += k[max_i] * capacity
            capacity = 0
        else:
            value += values[max_i]
            capacity -= weights[max_i]
        k[max_i] = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
