from math import sqrt, gcd, ceil, floor, log, factorial
from itertools import permutations, combinations
from collections import Counter, defaultdict

def dist(x1, x2):
    return abs(x1 - x2)

def power2(n):
    return ceil(log(n, 2)) == floor(log(n, 2))

def core_logic(x):
    flag1, flag2 = 0, 0
    d = Counter(x)

    for i in x:
        for po in range(0, 31):
            if d[i - pow(2, po)] > 0 and d[i + pow(2, po)] > 0:
                return 3, [i, i - pow(2, po), i + pow(2, po)]
        if flag1 == 1:
            break

    if flag1 == 0:
        for i in x:
            for po in range(0, 31):
                if d[i - pow(2, po)] > 0:
                    return 2, [i, i - pow(2, po)]
                elif d[i + pow(2, po)] > 0:
                    return 2, [i, i + pow(2, po)]
            if flag2 == 1:
                break

    if flag2 == 0:
        return 1, [max(x)]

def generate_input(n):
    if n <= 0:
        n = 1
    x = [i * 2 + (i % 3) for i in range(n)]
    return x

def main(n):
    x = generate_input(n)
    k, vals = core_logic(x)
    # print(k)
    pass
    # print(*vals)
    pass
if __name__ == "__main__":
    main(10)