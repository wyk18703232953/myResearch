from bisect import bisect_left
from collections import deque
from heapq import heappush, heappop
from math import gcd, ceil, sqrt, floor, inf
from itertools import groupby, permutations
from operator import add, mul, sub, xor, truediv, floordiv
from functools import reduce
from types import GeneratorType

#------------------------------------------------------------------------
# 原辅助函数，保留但不再使用输入输出加速

def A(n): return [0] * n
def AI(n, x): return [x] * n
def A2(n, m): return [[0] * m for _ in range(n)]
def G(n): return [[] for _ in range(n)]
def GP(it): return [[ch, len(list(g))] for ch, g in groupby(it)]

#------------------------------------------------------------------------

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

mod_default = 10**9 + 7
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
    ifa = []
    ifa.append(pow(farr[-1], mod - 2, mod))
    for i in range(x, 0, -1):
        ifa.append(ifa[-1] * i % mod)
    ifa.reverse()

def per(i, j, mod=0):
    if i < j: return 0
    if not mod:
        return fact(i) // fact(i - j)
    return farr[i] * ifa[i - j] % mod

def com(i, j, mod=0):
    if i < j: return 0
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
    if a <= 1: return a
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

class ST:
    def __init__(self, arr):  # n!=0
        n = len(arr)
        mx = n.bit_length()
        self.st = [[0] * mx for _ in range(n)]
        for i in range(n):
            self.st[i][0] = arr[i]
        for j in range(1, mx):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = max(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l, r):
        if l > r: return -inf
        s = (r + 1 - l).bit_length() - 1
        return max(self.st[l][s], self.st[r - (1 << s) + 1][s])

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

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.ranks = [0] * n
        self.size = AI(n, 1)
        self.edge = A(n)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            self.edge[pu] += 1
            return False
        if self.ranks[pu] >= self.ranks[pv]:
            self.parent[pv] = pu
            self.edge[pu] += self.edge[pv] + 1
            self.size[pu] += self.size[pv]
            if self.ranks[pv] == self.ranks[pu]:
                self.ranks[pu] += 1
        else:
            self.parent[pu] = pv
            self.edge[pv] += self.edge[pu] + 1
            self.size[pv] += self.size[pu]

def Prime(n):
    c = 0
    prime = []
    flag = [0] * (n + 1)
    for i in range(2, n + 1):
        if not flag[i]:
            prime.append(i)
            c += 1
        for j in range(c):
            if i * prime[j] > n: break
            flag[i * prime[j]] = prime[j]
            if i % prime[j] == 0: break
    return flag

def dij(s, graph, n):
    d = AI(n, inf)
    d[s] = 0
    heap = [(0, s)]
    vis = A(n)
    while heap:
        dis, u = heappop(heap)
        if vis[u]:
            continue
        vis[u] = 1
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heappush(heap, (d[v], v))
    return d

def bell(s, edge, n):
    dis = AI(n, inf)
    dis[s] = 0
    for _ in range(n - 1):
        for u, v, w in edge:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
    change = A(n)
    for _ in range(n):
        for u, v, w in edge:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                change[v] = 1
    return dis

def lcm(a, b): return a * b // gcd(a, b)

def lis(nums):
    res = []
    for k in nums:
        i = bisect_left(res, k)
        if i == len(res):
            res.append(k)
        else:
            res[i] = k
    return len(res)

def RP(nums):  # 逆序对
    n = len(nums)
    s = set(nums)
    d = {}
    for i, k in enumerate(sorted(s), 1):
        d[k] = i
    bi = BIT([0] * (len(s) + 1))
    ans = 0
    for i in range(n - 1, -1, -1):
        ans += bi.query(d[nums[i]] - 1)
        bi.update(d[nums[i]], 1)
    return ans

class DLN:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

def nb(i, j, n, m):
    for ni, nj in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
        if 0 <= ni < n and 0 <= nj < m:
            yield ni, nj

def topo(n, g, ind):
    q = deque()
    res = []
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i)
            res.append(i)
    while q:
        u = q.popleft()
        for v in g[u]:
            ind[v] -= 1
            if ind[v] == 0:
                q.append(v)
                res.append(v)
    return res

@bootstrap
def gdfs(r, p, g):
    for ch in g[r]:
        if ch != p:
            yield gdfs(ch, r, g)
    yield None

#------------------------------------------------------------------------
# 主逻辑封装为 main(n)，根据 n 生成测试数据 (n, mod)，并返回答案

def main(n):
    """
    将原先从输入读取 (n, mod) 的逻辑改为：
    - 使用参数 n 作为规模
    - 生成测试数据：mod = 10**9 + 7
    - 计算并返回答案
    """
    mod = mod_default

    # 预处理阶乘和逆阶乘
    ifact(n, mod)

    ma = (n + 1) // 2
    dp = A2(n + 1, ma + 1)
    f = A(n + 1)

    # 预计算 f[i] = 2^(i-1) (mod)
    if n >= 1:
        f[1] = 1
    if n >= 2:
        f[2] = 2
    if n >= 3:
        f[3] = 4
    for i in range(4, n + 1):
        f[i] = f[i - 1] * 2 % mod

    # 初始化 dp 的小规模值
    if n >= 1:
        dp[1][1] = 1
    if n >= 2:
        dp[2][1] = 2
    if n >= 3:
        dp[3][1] = 4
        dp[3][2] = 2

    # 状态转移
    for i in range(4, n + 1):
        dp[i][1] = f[i]
        lim_k = (i + 1) // 2
        for k in range(2, lim_k + 1):
            for x in range(1, i - 2 * k + 3):
                dp[i][k] += (
                    dp[i - x - 1][k - 1] *
                    f[x] % mod *
                    ifa[x] % mod *
                    fact(i - k + 1, mod) % mod *
                    ifa[i - k - x + 1] % mod
                )
                dp[i][k] %= mod

    ans = 0
    for k in range(1, ma + 1):
        ans = (ans + dp[n][k]) % mod

    return ans

# 如需快速自测，可解除以下注释：
# if __name__ == "__main__":
#     print(main(5))