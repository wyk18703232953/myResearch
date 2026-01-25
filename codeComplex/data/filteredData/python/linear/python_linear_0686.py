import sys
from collections import Counter

sys.setrecursionlimit(2000)

def core_algorithm(n, b):
    l = 0
    r = b[0]
    a = [0] * n
    for i in range(n // 2):
        a[i] = l
        a[n - 1 - i] = r
        if i != n // 2 - 1:
            val = b[i + 1]
            summ = l + r
            if summ == val:
                continue
            elif summ > val:
                diff = summ - val
                r -= diff
            else:
                diff = val - summ
                l += diff
    return a

def generate_b(n):
    half = max(1, n // 2)
    return [i + 1 for i in range(half)]

def main(n):
    b = generate_b(n)
    a = core_algorithm(n, b)
    for x in a:
        print(x, end=' ')
    print('')

if __name__ == "__main__":
    main(10)