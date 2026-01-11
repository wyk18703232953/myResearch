import math
import operator
from collections import OrderedDict

def binary(n):
    return (bin(n).replace("0b", ""))

def decimal(s):
    return (int(s, 2))

def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return (p)

def isPrime(n):
    if (n == 1):
        return (False)

    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if (n % i == 0):
                return (False)
        return (True)

def lts(l):
    s = ''.join(map(str, l))
    return s

def stl(s):
    l = list(s)
    return l

def sq(a, target, arr=[]):
    s = sum(arr)
    if (s == target):
        return arr
    if (s >= target):
        return
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if (ans):
            return ans

def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return (cnt)

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

mod = int(1e9) + 7

def main(n):
    # 映射：输入规模 n -> 原程序中的 m（数组长度）
    # 设原来的 n = m // 2，m = 2 * n
    m = max(1, 2 * n)
    n_val = m // 2

    # 构造确定性数组 a，长度为 m
    # 使用简单算术构造，使得有重复频率分布
    a = [(i // 3) % (n_val + 1) for i in range(m)]

    # 原核心逻辑开始
    n_orig = n_val
    m_orig = m

    if n_orig > m_orig:
        # print(0)
        pass
        return

    d = {}
    for c in a:
        if c in d:
            d[c] += 1

        else:
            d[c] = 1

    dict1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
    ans = 0
    for i in range(1, 105):
        temp = dict1.copy()
        n1 = n_orig
        for c in temp:
            n1 = n1 - (temp[c] // i)
        if n1 > 0:
            # print(i - 1)
            pass
            return

if __name__ == "__main__":
    main(1000)