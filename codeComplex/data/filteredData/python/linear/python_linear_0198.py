import math
from collections import Counter
from types import GeneratorType
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

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
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
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
        x = x // spf[x]
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

    else:
        ans = 0
        ti.sort()
        for i in ti:
            ans += (t - i) * (c - b) + a
        return ans

def main(n):
    # 生成规模为 n 的测试数据
    # 设定参数：
    # a: 初始得分
    # b: 初始增长系数
    # c: 后续增长系数
    # t: 最大时间
    a = 1
    b = 1
    c = 2
    t = n + 5  # 保证 t 大于所有 ti

    # 生成 ti: n 个在 [0, t] 范围内的时间点
    # 为了确定性，这里不用随机数，使用简单构造
    ti = [(i * 3) % (t + 1) for i in range(n)]

    ans = solve(n, a, b, c, t, ti)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)