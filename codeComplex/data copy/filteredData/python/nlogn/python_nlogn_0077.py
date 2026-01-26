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
    for i in range(2, int(n ** 0.5) + 1):
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
        for i in range(2, int(n ** 0.5) + 1):
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

def generate_data(n):
    # n is the number of (x, y) pairs
    # k is chosen deterministically based on n
    k = n // 2 + 1 if n > 0 else 1
    arr = []
    for i in range(n):
        # Deterministic construction of (x, y)
        # x groups repeated values to create ties, y varies
        x = i // 3
        y = (i * 2 + 1) % (n + 3)
        arr.append((x, y))
    return n, k, arr

def core_logic(n, k, arr):
    arr = sorted(arr, key=lambda x: x[0], reverse=True)

    # Preserve the original O(n^2) stable-by-second-key behavior
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] and arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]

    cnt = arr.count(arr[k - 1])
    return cnt

def main(n):
    n, k, arr = generate_data(n)
    result = core_logic(n, k, arr)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)