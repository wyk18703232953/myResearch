from bisect import *
from collections import *
from math import gcd, ceil, sqrt, floor, inf
from heapq import *
from itertools import *
from operator import add, mul, sub, xor, truediv, floordiv
from functools import *
from types import GeneratorType

mod = 10**9 + 7
farr = [1]
ifa = []


def fact(x, mod=0):
    if mod:
        while x >= len(farr):
            farr.append(farr[-1] * len(farr) % mod)
    else:
        while x >= len(farr):
            farr.append(farr[-1] * len(farr))
    return farr[x]


def ifact(x, mod):
    global ifa
    fact(x, mod)
    ifa.append(pow(farr[-1], mod - 2, mod))
    for i in range(x, 0, -1):
        ifa.append(ifa[-1] * i % mod)
    ifa.reverse()


def per(i, j, mod=0):
    if i < j:
        return 0
    if not mod:
        return fact(i) // fact(i - j)
    return farr[i] * ifa[i - j] % mod


def com(i, j, mod=0):
    if i < j:
        return 0
    if not mod:
        return per(i, j) // fact(j)
    return per(i, j, mod) * ifa[j] % mod


def catalan(n):
    return com(2 * n, n) // (n + 1)


def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def floorsum(a, b, c, n):  # sum((a*i+b)//c for i in range(n+1))
    if a == 0:
        return b // c * (n + 1)
    if a >= c or b >= c:
        return floorsum(a % c, b % c, c, n) + b // c * (n + 1) + a // c * n * (n + 1) // 2
    m = (a * n + b) // c
    return n * m - floorsum(c, c - b - 1, a, m - 1)


def inverse(a, m):
    a %= m
    if a <= 1:
        return a
    return ((1 - inverse(m, a) * m) // a) % m


def lowbit(n):
    return n & -n


class BIT:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr) - 1

    def update(self, x, v):
        while x <= self.n:
            self.arr[x] += v
            x += x & -x

    def query(self, x):
        ans = 0
        while x:
            ans += self.arr[x]
            x &= x - 1
        return ans


class DSU:
    def __init__(self, n):
        self.c = [-1] * n

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.c[x] < 0:
            return x
        self.c[x] = self.find(self.c[x])
        return self.c[x]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if self.c[u] > self.c[v]:
            u, v = v, u
        self.c[u] += self.c[v]
        self.c[v] = u
        return True

    def size(self, x):
        return -self.c[self.find(x)]


class UFS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] >= self.ranks[pv]:
            self.parent[pv] = pu
            if self.ranks[pv] == self.ranks[pu]:
                self.ranks[pu] += 1
        else:
            self.parent[pu] = pv


def Prime(n):
    c = 0
    prime = []
    flag = [0] * (n + 1)
    for i in range(2, n + 1):
        if not flag[i]:
            prime.append(i)
            c += 1
        for j in range(c):
            if i * prime[j] > n:
                break
            flag[i * prime[j]] = prime[j]
            if i % prime[j] == 0:
                break
    return prime


def dij(s, graph):
    d = {}
    d[s] = 0
    heap = [(0, s)]
    seen = set()
    while heap:
        dis, u = heappop(heap)
        if u in seen:
            continue
        seen.add(u)
        for v, w in graph[u]:
            if v not in d or d[v] > d[u] + w:
                d[v] = d[u] + w
                heappush(heap, (d[v], v))
    return d


def GP(it):
    return [[ch, len(list(g))] for ch, g in groupby(it)]


def lcm(a, b):
    return a * b // gcd(a, b)


def lis(nums):
    res = []
    for k in nums:
        i = bisect_left(res, k)
        if i == len(res):
            res.append(k)
        else:
            res[i] = k
    return len(res)


class DLN:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


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


def match(pat, cur, k):
    for i in range(k):
        if pat[i] != '_' and pat[i] != cur[i]:
            return False
    return True


@bootstrap
def gdfs(r, p, g):
    if len(g[r]) == 1 and p != -1:
        yield None
    for ch in g[r]:
        if ch != p:
            yield gdfs(ch, r, g)
    yield None


def pos(cur, k):
    res = list(cur)
    pa = []
    dfs(0, pa, res, k)
    return pa


def dfs(i, pa, res, k):
    if i == k:
        pa.append(''.join(res))
        return
    dfs(i + 1, pa, res, k)
    tmp = res[i]
    res[i] = '_'
    dfs(i + 1, pa, res, k)
    res[i] = tmp


def topo(n, g, ind):
    q = deque()
    res = []
    for i in range(n):
        if ind[i] == 0:
            q.append(i)
            res.append(i + 1)
    while q:
        u = q.popleft()
        for v in g[u]:
            ind[v] -= 1
            if ind[v] == 0:
                q.append(v)
                res.append(v + 1)
    return res


def generate_input(n):
    n_val = max(1, n)
    k = max(1, n_val // 2)
    m = n_val
    patterns = []
    for i in range(n_val):
        base = []
        for j in range(k):
            base.append(chr(ord('a') + (i + j) % 3))
        patterns.append(''.join(base))
    queries = []
    for i in range(m):
        idx = i % n_val
        cur = list(patterns[idx])
        for j in range(k):
            if (i + j) % 3 == 0:
                cur[j] = '_'
        queries.append((''.join(cur), idx + 1))
    return n_val, m, k, patterns, queries


def main(n):
    n_val, m, k, p, query_list = generate_input(n)
    d = {p[i]: i for i in range(n_val)}
    ans = True
    ind = [0] * n_val
    g = [[] for _ in range(n_val)]
    for cur, x in query_list:
        if ans:
            if not match(p[x - 1], cur, k):
                ans = False
            else:
                for al in pos(cur, k):
                    if al in d and d[al] != x - 1:
                        g[x - 1].append(d[al])
                        ind[d[al]] += 1
    if not ans:
        print("NO")
    else:
        order = topo(n_val, g, ind)
        if len(order) != n_val:
            print("NO")
        else:
            print("YES")
            print(*order)


if __name__ == "__main__":
    main(5)