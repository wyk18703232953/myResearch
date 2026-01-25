import math
from collections import defaultdict

alphabets = list('abcdefghijklmnopqrstuvwxyz')

def bootstrap(f, stack=[]):
    from types import GeneratorType
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

def generate_data(n):
    if n <= 0:
        n = 1
    c = [0] * (n + 1)
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i] = (i * 7) % (n + 3) + 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            a[i] = i // 2
        else:
            a[i] = i + 1 if i < n else 1
    return n, c, a

def core_solve(n, c, a):
    vis = [False] * (n + 1)
    ans = 0
    d = defaultdict(lambda: 0)
    cycleno = 0
    for i in range(1, n + 1):
        if not vis[i]:
            cur = i
            while not vis[cur]:
                d[cur] = cycleno
                vis[cur] = True
                cur = a[cur]
            if d[cur] == cycleno:
                min_ = c[cur]
                first = cur
                cur = a[cur]
                while first != cur:
                    min_ = min(c[cur], min_)
                    cur = a[cur]
                ans += min_
            cycleno += 1
    return ans

def main(n):
    n_gen, c, a = generate_data(n)
    result = core_solve(n_gen, c, a)
    print(result)

if __name__ == "__main__":
    main(10)