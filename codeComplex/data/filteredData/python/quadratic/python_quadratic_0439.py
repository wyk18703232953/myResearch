import sys
import math
import bisect
from random import randint
from collections import deque, defaultdict, Counter
import heapq
import string

inf = float('inf')
mod = 998244353

"========================================"


def lcm(a, b):
    return int((a / math.gcd(a, b)) * b)


def gcd(a, b):
    return int(math.gcd(a, b))


def tobinary(n):
    return bin(n)[2:]


def binarySearch(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def lowerBound(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1


def upperBound(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a) + 1 and a[i - 1] == x:
        return i - 1
    else:
        return -1


def primesInRange(n):
    ans = []
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            ans.append(p)
    return ans


def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


def isPrime(n, k=5):
    if n < 2:
        return True
    for _ in range(k):
        a = randint(1, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


"========================================="


def main(n):
    # 生成长度为 n 的随机数字串，字符为 '0'~'9'
    s = [randint(0, 9) for _ in range(n)]

    for target_sum in range(0, (9 * n) + 1):
        count = 0
        cur_sum = 0
        for digit in s:
            cur_sum += digit
            if cur_sum == target_sum:
                count += 1
                cur_sum = 0
        if count > 1 and cur_sum == 0:
            print('YES')
            return
    print('NO')


if __name__ == "__main__":
    # 示例：可以根据需要修改这里的 n 来做简单测试
    main(5)