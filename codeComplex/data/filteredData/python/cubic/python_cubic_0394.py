from bisect import bisect, bisect_left
from collections import *
from math import gcd, ceil, sqrt, floor, inf
from heapq import *
from itertools import *
from operator import add, mul, sub, xor, truediv, floordiv
from functools import *
import random

mod = 10 ** 9 + 7
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
    for i in range(2, int(n ** 0.5) + 1):
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


class ST:
    def __init__(self, arr):  # n!=0
        n = len(arr)
        mx = n.bit_length()  # 取不到
        self.st = [[0] * mx for _ in range(n)]
        for i in range(n):
            self.st[i][0] = arr[i]
        for j in range(1, mx):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = max(self.st[i][j - 1], self.st[i + (1 << j - 1)][j - 1])

    def query(self, l, r):
        if l > r:
            return -inf
        s = (r + 1 - l).bit_length() - 1
        return max(self.st[l][s], self.st[r - (1 << s) + 1][s])


class DSU:  # 容量+路径压缩
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


class UFS:  # 秩+路径
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
    return flag


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


def bell(s, g, n, edge):  # bellman-Ford
    dis = [inf] * n
    dis[s] = 0
    for _ in range(n - 1):
        for u, v, w in edge:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
    change = [0] * n
    for _ in range(n):
        for u, v, w in edge:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                change[v] = 1
    return dis


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


def main(n):
    # 规模 n 控制网格大小，生成一个接近正方形的 n 个格子的网格
    if n <= 0:
        return
    m = int(sqrt(n))
    if m == 0:
        m = 1
    rows = max(1, n // m)
    if rows * m < n:
        rows += 1
    # 限制一下，避免过大
    rows = min(rows, 200)
    m = min(m, 200)

    # k 为偶数步长；这里选一个相对适中的值
    k = 2 * max(1, (rows + m) // 2)

    # 生成测试数据：h 为横边权，v 为竖边权
    # h: rows x (m-1), v: (rows-1) x m
    rand = random.Random(0)
    h = [[rand.randint(1, 10) for _ in range(m - 1)] for _ in range(rows)]
    v = [[rand.randint(1, 10) for _ in range(m)] for _ in range(rows - 1)]

    # 若 k 为奇数，输出 -1；这里 k 已保证为偶数，但保留逻辑
    if k & 1:
        for _ in range(rows):
            print(*([-1] * m))
        return

    k //= 2
    dp = [[[inf] * m for _ in range(rows)] for _ in range(k + 1)]
    for i in range(rows):
        for j in range(m):
            dp[0][i][j] = 0

    for step in range(1, k + 1):
        for i in range(rows):
            for j in range(m):
                cur = inf
                if i:
                    cur = min(cur, dp[step - 1][i - 1][j] + 2 * v[i - 1][j])
                if i + 1 < rows:
                    cur = min(cur, dp[step - 1][i + 1][j] + 2 * v[i][j])
                if j:
                    cur = min(cur, dp[step - 1][i][j - 1] + 2 * h[i][j - 1])
                if j + 1 < m:
                    cur = min(cur, dp[step - 1][i][j + 1] + 2 * h[i][j])
                dp[step][i][j] = cur

    for i in range(rows):
        res = []
        for j in range(m):
            res.append(dp[k][i][j])
        print(*res)


if __name__ == "__main__":
    # 示例：规模参数 n，可自行调整
    main(20)