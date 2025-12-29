from collections import defaultdict as dd
import random

def solve_one(arr):
    l1 = dd(int)
    a = 0
    for j in arr:
        l1[j] += 1
        if l1[j] == 4:
            a = j
    if a:
        return [a, a, a, a]
    else:
        c = 0
        x = 0
        l2 = []
        for j in l1:
            if l1[j] >= 2:
                l2.append(j)
        l2.sort()
        a = b = 0
        for j in l2:
            c += 1
            if c == 1:
                a = j
            elif c == 2:
                b = j
            else:
                if x / j + j / x < a / b + b / a:
                    a, b = x, j
            x = j
        return [a, a, b, b]

def main(n):
    random.seed(0)
    t = 3  # number of test cases
    for _ in range(t):
        # Generate an array of length n with values in [1, n]
        arr = [random.randint(1, n) for _ in range(n)]
        res = solve_one(arr)
        print(*res)

if __name__ == "__main__":
    main(10)