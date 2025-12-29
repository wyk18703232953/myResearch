import random
import math
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

alphabets = list('abcdefghijklmnopqrstuvwxyz')


# for deep recursion__________________________________________-
from types import GeneratorType
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
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    c = dict(Counter(l))
    return list(set(l))
    # return c

def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res

#____________________GetPrimeFactors in log(n)________________________________________
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
        x = x // spf[x]
    return ret
#____________________________________________________________

def SieveOfEratosthenes(n):
    # time complexity = nlog(log(n))
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
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


def main(n: int):
    # 生成测试数据
    # n: 数组长度
    # 约定：
    # 1 <= n
    n = max(1, int(n))

    # 生成 a, b, c, t
    # 让时间范围和奖励大小大致与 n 有关，但避免溢出
    max_time = max(10, n * 2)
    a = random.randint(1, 10**3)
    b = random.randint(0, 10**3)
    c = random.randint(0, 10**3)
    t = random.randint(1, max_time)

    # 生成 ti：每个在 [0, t] 范围内
    ti = [random.randint(0, t) for _ in range(n)]

    ans = solve(n, a, b, c, t, ti)
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)