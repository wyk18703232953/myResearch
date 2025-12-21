from math import sqrt, gcd, ceil, floor, log, factorial
from itertools import permutations, combinations
from collections import Counter, defaultdict
import random

def dist(x1, x2):
    return abs(x1 - x2)

def power2(n):
    return ceil(log(n, 2)) == floor(log(n, 2))

def main(n):
    random.seed(0)
    x = [random.randint(0, 10**9) for _ in range(n)]
    flag1, flag2, flag3 = 0, 0, 0
    d = Counter(x)
    for i in x:
        for po in range(0, 31):
            if d[i - pow(2, po)] > 0 and d[i + pow(2, po)] > 0:
                print(3)
                print(i, i - pow(2, po), i + pow(2, po))
                flag1 = 1
                break
        if flag1 == 1:
            break
    if flag1 == 0:
        for i in x:
            for po in range(0, 31):
                if d[i - pow(2, po)] > 0:
                    print(2)
                    print(i, i - pow(2, po))
                    flag2 = 1
                    break
                elif d[i + pow(2, po)] > 0:
                    print(2)
                    print(i, i + pow(2, po))
                    flag2 = 1
                    break
            if flag2 == 1:
                break
        if flag2 == 0:
            print(1)
            print(max(x))

if __name__ == "__main__":
    main(10)