import math


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
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n / i
    if n > 2:
        l.append(int(n))
    return l


def primeFactorsCount(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            cnt += 1
            n = n // i
    if n > 2:
        cnt += 1
    return cnt


def isPrime(n):
    if n == 1:
        return False

    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if n % i == 0:
                return False
        return True


def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def countcon(s, i):
    c = 0
    ch = s[i]
    for i in range(i, len(s)):
        if s[i] == ch:
            c += 1

        else:
            break
    return c


def lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, dp[i])
    return maximum


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0
    i = 0
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1
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
    primes = [True] * (n + 1)
    primes[1] = primes[0] = False
    i = 2
    while i * i <= n:
        if primes[i] is True:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    pr = []
    for i in range(0, n + 1):
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


def chk1(i, n, l1, l2):
    if i != n - 1 and l1[i] == l2[i] == l2[i + 1] == "0":
        l1[i] = l2[i] = l2[i + 1] = "X"
        return True
    return False


def chk2(i, n, l1, l2):
    if i != n - 1 and l1[i] == l1[i + 1] == l2[i] == "0":
        l1[i] = l1[i + 1] = l2[i] = "X"
        return True
    return False


def chk3(i, n, l1, l2):
    if i != n - 1 and l1[i] == l1[i + 1] == l2[i + 1] == "0":
        l1[i] = l1[i + 1] = l2[i + 1] = "X"
        return True
    return False


def chk4(i, n, l1, l2):
    if i != n - 1 and l2[i + 1] == l1[i + 1] == l2[i] == "0":
        l1[i] = l1[i + 1] = l2[i] = "X"
        return True
    return False


def check1(i, n, l1, l2):
    if i <= n - 3 and l1[i:i + 3] == l2[i:i + 3] == ["0", "0", "0"]:
        for j in range(i, i + 3):
            l1[j] = l2[j] = "X"
        return True
    return False


def check2(i, n, l1, l2):
    if chk1(i, n, l1, l2) or chk2(i, n, l1, l2) or chk3(i, n, l1, l2) or chk4(i, n, l1, l2):
        return True
    return False


def run_core(l1, l2):
    n = len(l1)
    i = 0
    ans = 0
    while i < n:
        if check1(i, n, l1, l2):
            ans += 2
            i += 3

        else:
            if check2(i, n, l1, l2):
                ans += 1
                i += 2

            else:
                i += 1
    return ans


def generate_rows(n):
    if n <= 0:
        return [], []
    # deterministic pattern based on index
    l1 = []
    l2 = []
    for i in range(n):
        # l1: 0 when i%3==0 or i%5==0, else 1
        l1.append("0" if (i % 3 == 0 or i % 5 == 0) else "1")
        # l2: 0 when (i%2==0 and i%4!=0) or i%7==0, else 1
        cond2 = (i % 2 == 0 and i % 4 != 0) or (i % 7 == 0)
        l2.append("0" if cond2 else "1")
    return l1, l2


def main(n):
    if n < 0:
        n = 0
    l1, l2 = generate_rows(n)
    ans = run_core(l1, l2)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)