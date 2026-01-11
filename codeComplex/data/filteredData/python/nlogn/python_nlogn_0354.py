import math
from collections import deque, defaultdict
import operator as op
from functools import reduce
from itertools import permutations
import heapq

alpha = "abcdefghijklmnopqrstuvwxyz"


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def isPrime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True

    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def main(n):
    # Deterministic generation of array of length n
    # Example pattern: arr[i] = i % 1000 to keep values bounded and allow repetitions
    arr = [i % 1000 for i in range(n)]

    sett = set(arr)

    power = [2 ** i for i in range(32)]

    ans = []

    for i in power:
        for j in arr:
            tmp = [j]
            for _ in range(2):
                if tmp[-1] + i in sett:
                    tmp.append(tmp[-1] + i)

            if len(tmp) > len(ans):
                ans = [x for x in tmp]

            if len(ans) == 3:
                break

        if len(ans) == 3:
            break

    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass
if __name__ == "__main__":
    main(10000)