import math
import random

mod = 1000000007


def binary(n):
    return bin(n).replace("0b", "")


def decimal(s):
    return int(s, 2)


def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n // i
    if n > 2:
        l.append(int(n))
    return l


def primeFactorsCount(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n = n // 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            cnt += 1
            n = n // i
    if n > 2:
        cnt += 1
    return cnt


def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True


def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n // i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def countcon(s, i):
    c = 0
    ch = s[i]
    for j in range(i, len(s)):
        if s[j] == ch:
            c += 1
        else:
            break
    return c


def lis(arr):
    n = len(arr)
    lis_arr = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_arr[i] < lis_arr[j] + 1:
                lis_arr[i] = lis_arr[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis_arr[i])
    return maximum


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j += 1
        i += 1
    return j == m


def maxfac(n):
    root = int(n ** 0.5)
    for i in range(2, root + 1):
        if n % i == 0:
            return n // i
    return n


def p2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def seive(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    pr = []
    for i in range(2, n + 1):
        if primes[i]:
            pr.append(i)
    return pr


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def denofactinverse(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return pow(fac, m - 2, m)


def numofact(n, m):
    fac = 1
    for i in range(1, n + 1):
        fac = (fac * i) % m
    return fac


def sod(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def main(n):
    # 根据规模 n 生成测试数据：
    # 让 x 和 k 随着 n 增大而适度增大
    random.seed(n)
    x = random.randint(0, 10 ** (min(n, 9)))  # 防止过大溢出，控制在 1e9 量级
    k = random.randint(0, max(1, n))

    tp = pow(2, k + 1, mod)
    tp2 = pow(2, k, mod)
    ans = (tp * x - tp2 + 1) % mod
    result = ans if x != 0 else 0
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用 n=10 调用
    main(10)