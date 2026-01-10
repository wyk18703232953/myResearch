import math
from heapq import *

gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil

def ind(ch):
    return ord(ch) - ord("a")

def cleanarr(arr):
    n = len(arr)
    arr.sort()
    c = []
    curr = [arr[0], 1]
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            if curr[1] >= 2:
                c.append(curr)
            curr = [arr[i + 1], 1]
        else:
            curr[1] += 1
    if curr[1] >= 2:
        c.append(curr)
    return c

def run_single_case(n):
    arr = [(i % (max(1, n // 10))) + 1 for i in range(n)]
    g = arr[0]
    c = cleanarr(arr)
    if n >= 40000:
        f = 0
        for i in range(len(c)):
            if c[i][1] >= 4:
                f = c[i][0]
                break
        print(f, " ")
        print(f, " ")
        print(f, " ")
        print(f, "\n")
        return
    mi = 10**18
    pair = [-1, -1]
    for i in range(len(c)):
        if c[i][1] >= 4:
            pair = [c[i][0], c[i][0]]
            break
        if i == len(c) - 1:
            break
        a = c[i][0]
        b = c[i + 1][0]
        if mi == 10**18:
            pair = [a, b]
            mi = 0
            continue
        if ((((pair[0] + pair[1]) ** 2) * a * b) - (((a + b) ** 2) * pair[0] * pair[1]) > 0):
            pair = [a, b]
    print(pair[0], " ")
    print(pair[0], " ")
    print(pair[1], " ")
    print(pair[1], "\n")

def main(n):
    t = 3
    sizes = [n, max(1, n // 2), max(1, n * 2)]
    for i in range(t):
        run_single_case(sizes[i % len(sizes)])

if __name__ == "__main__":
    main(100000)