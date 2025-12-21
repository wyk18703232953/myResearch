from collections import Counter
import random

def main(n):
    m = n // 2
    l = [m] * n
    p = n // 2
    le, ri = Counter(), Counter()
    c = 0
    le[0] = ri[0] = 1
    for i in range(p + 1, n):
        if l[i] < m:
            c += 1
        else:
            c -= 1
        ri[c] += 1
    c = 0
    for i in range(p - 1, -1, -1):
        if l[i] < m:
            c -= 1
        else:
            c += 1
        le[c] += 1
    res = 0
    for c, x in le.items():
        res += x * (ri[c] + ri[c - 1])
    return res

if __name__ == '__main__':
    print(main(10))