import math
from collections import deque, defaultdict
import operator as op
from functools import reduce
from itertools import permutations

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


def core_logic(arr):
    sett = set(arr)
    ans = [arr[0]]
    flag = 0
    for x in range(31):
        d = 1 << x
        for i in arr:
            if (i - d) in sett and (i + d) in sett:
                ans = [i - d, i, i + d]
                flag = 1
                break
            elif (i - d) in sett:
                ans = [i - d, i]
            elif (i + d) in sett:
                ans = [i, i + d]
        if flag:
            break
    return ans


def generate_input(n):
    if n <= 0:
        n = 1
    arr = [i for i in range(1, n + 1)]
    return arr


def main(n):
    arr = generate_input(n)
    ans = core_logic(arr)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main(10)