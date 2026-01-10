import math
from collections import deque, defaultdict
import operator as op
from functools import reduce
from itertools import permutations

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def valid(row, col, rows, cols, rcross, lcross):
    return rows[row] == 0 and cols[col] == 0 and rcross[col + row] == 0 and lcross[col - row] == 0

def div(n):
    if n == 1:
        return 1
    cnt = 2
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            if i != n // i:
                cnt += 2
            else:
                cnt += 1
    return cnt

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    else:
        flag = True
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                flag = False
                break
        return flag

def s(b):
    ans = []
    while b > 0:
        tmp = b % 10
        ans.append(tmp)
        b = b // 10
    return ans

def main(n):
    # n controls the input size: number of pairs
    if n <= 0:
        print(0)
        return

    k = (n + 1) // 2
    arr = []
    for i in range(n):
        x = i + 1
        y = (i * 2 + 3)
        arr.append((-x, y))

    arr.sort()
    target = arr[k - 1]
    cnt = arr.count(target)
    print(cnt)

if __name__ == "__main__":
    main(10)