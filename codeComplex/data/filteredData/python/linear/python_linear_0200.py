import random
import math
from collections import Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from types import GeneratorType

alphabets = list('abcdefghijklmnopqrstuvwxyz')

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n // i
    if n > 2:
        l.append(n)
    c = dict(Counter(l))
    return list(set(l))

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def sieveForSmallestPrimeFactor():
    MAXN = 100001
    spf = [0 for _ in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def getPrimeFactorizationLOGN(x):
    spf = sieveForSmallestPrimeFactor()
    ret = []
    while x != 1:
        ret.append(spf[x])
        x //= spf[x]
    return ret

def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1

def solve(n, a, b, c, t, ti):
    if b > c:
        return n * a
    ans = 0
    ti.sort()
    for i in ti:
        ans += (t - i) * (c - b) + a
    return ans

def main(n):
    # 生成测试数据
    # n: 数组 ti 的长度
    # 为了保证 (t - ti[i]) 非负，令 t 为 [1, 2n] 区间内的数，
    # ti[i] 在 [0, t] 区间内
    random.seed(0)

    # 生成参数 a, b, c, t
    a = random.randint(1, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    t = random.randint(1, 2 * max(1, n))

    ti = [random.randint(0, t) for _ in range(n)]

    ans = solve(n, a, b, c, t, ti)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)