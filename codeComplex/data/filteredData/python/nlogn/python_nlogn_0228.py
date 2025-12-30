import random

# ----------------- 原有工具函数与类（未使用部分保留以保持结构完整） -----------------

def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i = i + 1
    return d

def popcount(x):
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    return x & 0x0000007f

def eratosthenes(n):
    res = [0 for _ in range(n + 1)]
    prime = set([])
    for i in range(2, n + 1):
        if not res[i]:
            prime.add(i)
            for j in range(1, n // i + 1):
                res[i * j] = 1
    return prime

def factorization(n):
    res = []
    for p in prime:
        if n % p == 0:
            while n % p == 0:
                n //= p
            res.append(p)
    if n != 1:
        res.append(n)
    return res

def euler_phi(n):
    res = n
    for x in range(2, n + 1):
        if x ** 2 > n:
            break
        if n % x == 0:
            res = res // x * (x - 1)
            while n % x == 0:
                n //= x
    if n != 1:
        res = res // n * (n - 1)
    return res

def ind(b, n):
    res = 0
    while n % b == 0:
        res += 1
        n //= b
    return res

def isPrimeMR(n):
    if n < 2:
        return 0
    d = n - 1
    d = d // (d & -d)
    L = [2, 3, 5, 7, 11, 13, 17]
    for a in L:
        if a % n == 0:
            continue
        t = d
        y = pow(a, t, n)
        if y == 1 or y == n - 1:
            continue
        while True:
            y = (y * y) % n
            t <<= 1
            if y == 1:
                return 0
            if y == n - 1:
                break
            if t >= n - 1:
                return 0
    return 1

def findFactorRho(n):
    from math import gcd
    if n % 2 == 0:
        return 2
    m = 1 << (n.bit_length() // 8)
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)

def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret

def divisors2(n):
    res = [1]
    prime = primeFactor(n)
    for p in prime:
        newres = []
        for d in res:
            for j in range(prime[p] + 1):
                newres.append(d * p ** j)
        res = newres
    res.sort()
    return res

def xorconv(n, X, Y, mod=10**9+7):
    inv = pow(2, -1, mod)
    if n == 0:
        res = [(X[0] * Y[0]) % mod]
        return res
    half = 1 << (n - 1)
    x = [X[i] + X[i + half] for i in range(half)]
    y = [Y[i] + Y[i + half] for i in range(half)]
    z = [X[i] - X[i + half] for i in range(half)]
    w = [Y[i] - Y[i + half] for i in range(half)]
    res1 = xorconv(n - 1, x, y, mod)
    res2 = xorconv(n - 1, z, w, mod)
    former = [(res1[i] + res2[i]) * inv for i in range(half)]
    latter = [(res1[i] - res2[i]) * inv for i in range(half)]
    former = list(map(lambda x: x % mod, former))
    latter = list(map(lambda x: x % mod, latter))
    return former + latter

def merge_sort(A, B):
    pos_A, pos_B = 0, 0
    n, m = len(A), len(B)
    res = []
    while pos_A < n and pos_B < m:
        a, b = A[pos_A], B[pos_B]
        if a < b:
            res.append(a)
            pos_A += 1
        else:
            res.append(b)
            pos_B += 1
    res += A[pos_A:]
    res += B[pos_B:]
    return res

class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N
        self.group = N

    def find_root(self, x):
        if self._parent[x] == x:
            return x
        self._parent[x] = self.find_root(self._parent[x])
        stack = [x]
        while self._parent[stack[-1]] != stack[-1]:
            stack.append(self._parent[stack[-1]])
        for v in stack:
            self._parent[v] = stack[-1]
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy:
            return

        self.group -= 1

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

class WeightedUnionFind():
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]
        self.val = [0 for _ in range(N)]
        self.flag = True
        self.edge = [[] for _ in range(N)]

    def dfs(self, v, pv):
        stack = [(v, pv)]
        new_parent = self.parent[pv]
        while stack:
            v, pv = stack.pop()
            self.parent[v] = new_parent
            for nv, w in self.edge[v]:
                if nv != pv:
                    self.val[nv] = self.val[v] + w
                    stack.append((nv, v))

    def unite(self, x, y, w):
        if not self.flag:
            return
        if self.parent[x] == self.parent[y]:
            self.flag = (self.val[x] - self.val[y] == w)
            return

        if self.size[self.parent[x]] > self.size[self.parent[y]]:
            self.edge[x].append((y, -w))
            self.edge[y].append((x, w))
            self.size[x] += self.size[y]
            self.val[y] = self.val[x] - w
            self.dfs(y, x)
        else:
            self.edge[x].append((y, -w))
            self.edge[y].append((x, w))
            self.size[y] += self.size[x]
            self.val[x] = self.val[y] + w
            self.dfs(x, y)

class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        self.G = [[] for _ in range(V)]
        self._E = 0
        self._V = V

    @property
    def E(self):
        return self._E

    @property
    def V(self):
        return self._V

    def add_edge(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        import heapq
        que = []
        d = [10 ** 15] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost:
                continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    heapq.heappush(que, (d[e.to], e.to))
        return d

def Z_algorithm(s):
    N = len(s)
    Z_alg = [0] * N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i + j < N and s[j] == s[i + j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < N and k + Z_alg[k] < j:
            Z_alg[i + k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg

class BIT():
    def __init__(self, n):
        self.BIT = [0] * (n + 1)
        self.num = n

    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    def update(self, idx, x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx & (-idx)
        return

class dancinglink():
    def __init__(self, n, debug=False):
        self.n = n
        self.debug = debug
        self._left = [i - 1 for i in range(n)]
        self._right = [i + 1 for i in range(n)]
        self.exist = [True for _ in range(n)]

    def pop(self, k):
        if self.debug:
            assert self.exist[k]
        L = self._left[k]
        R = self._right[k]
        if L != -1:
            if R != self.n:
                self._right[L], self._left[R] = R, L
            else:
                self._right[L] = self.n
        elif R != self.n:
            self._left[R] = -1
        self.exist[k] = False

    def left(self, idx, k=1):
        if self.debug:
            assert self.exist[idx]
        res = idx
        while k:
            res = self._left[res]
            if res == -1:
                break
            k -= 1
        return res

    def right(self, idx, k=1):
        if self.debug:
            assert self.exist[idx]
        res = idx
        while k:
            res = self._right[res]
            if res == self.n:
                break
            k -= 1
        return res

class SparseTable():
    def __init__(self, A, merge_func, ide_ele):
        N = len(A)
        n = N.bit_length()
        self.table = [[ide_ele for _ in range(n)] for _ in range(N)]
        self.merge_func = merge_func

        for i in range(N):
            self.table[i][0] = A[i]

        for j in range(1, n):
            for i in range(0, N - 2 ** j + 1):
                f = self.table[i][j - 1]
                s = self.table[i + 2 ** (j - 1)][j - 1]
                self.table[i][j] = self.merge_func(f, s)

    def query(self, s, t):
        b = t - s + 1
        m = b.bit_length() - 1
        return self.merge_func(self.table[s][m], self.table[t - 2 ** m + 1][m])

class BinaryTrie:
    class node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.max = val

    def __init__(self):
        self.root = self.node(-10 ** 15)

    def append(self, key, val):
        pos = self.root
        for i in range(29, -1, -1):
            pos.max = max(pos.max, val)
            if key >> i & 1:
                if pos.right is None:
                    pos.right = self.node(val)
                    pos = pos.right
                else:
                    pos = pos.right
            else:
                if pos.left is None:
                    pos.left = self.node(val)
                    pos = pos.left
                else:
                    pos = pos.left
        pos.max = max(pos.max, val)

    def search(self, M, xor):
        res = -10 ** 15
        pos = self.root
        for i in range(29, -1, -1):
            if pos is None:
                break

            if M >> i & 1:
                if xor >> i & 1:
                    if pos.right:
                        res = max(res, pos.right.max)
                    pos = pos.left
                else:
                    if pos.left:
                        res = max(res, pos.left.max)
                    pos = pos.right
            else:
                if xor >> i & 1:
                    pos = pos.right
                else:
                    pos = pos.left

        if pos:
            res = max(res, pos.max)
        return res

def solveequation(edge, ans, n, m):
    # edge=[[to,dire,id]...]
    x = [0] * m
    used = [False] * n

    def dfs(v):
        used[v] = True
        r = ans[v]
        for to, dire, idx in edge[v]:
            if used[to]:
                continue
            y = dfs(to)
            if dire == -1:
                x[idx] = y
            else:
                x[idx] = -y
            r += y
        return r

    for v in range(n):
        if used[v]:
            continue
        y = dfs(v)
        if y != 0:
            return False
    return x

class Matrix():
    mod = 10 ** 9 + 7

    @staticmethod
    def set_mod(m):
        Matrix.mod = m

    def __init__(self, L):
        self.row = len(L)
        self.column = len(L[0])
        self._matrix = L
        for i in range(self.row):
            for j in range(self.column):
                self._matrix[i][j] %= Matrix.mod

    def __getitem__(self, item):
        if isinstance(item, int):
            raise IndexError("you must specific row and column")
        elif len(item) != 2:
            raise IndexError("you must specific row and column")

        i, j = item
        return self._matrix[i][j]

    def __setitem__(self, item, val):
        if isinstance(item, int):
            raise IndexError("you must specific row and column")
        elif len(item) != 2:
            raise IndexError("you must specific row and column")

        i, j = item
        self._matrix[i][j] = val

    def __add__(self, other):
        if (self.row, self.column) != (other.row, other.column):
            raise Exception("sizes of matrixes are different")

        res = [[0 for _ in range(self.column)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                res[i][j] = self._matrix[i][j] + other._matrix[i][j]
                res[i][j] %= Matrix.mod
        return Matrix(res)

    def __sub__(self, other):
        if (self.row, self.column) != (other.row, other.column):
            raise Exception("sizes of matrixes are different")

        res = [[0 for _ in range(self.column)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                res[i][j] = self._matrix[i][j] - other._matrix[i][j]
                res[i][j] %= Matrix.mod
        return Matrix(res)

    def __mul__(self, other):
        if not isinstance(other, int):
            if self.column != other.row:
                raise Exception("sizes of matrixes are different")

            res = [[0 for _ in range(other.column)] for _ in range(self.row)]
            for i in range(self.row):
                for j in range(other.column):
                    temp = 0
                    for k in range(self.column):
                        temp += self._matrix[i][k] * other._matrix[k][j]
                    res[i][j] = temp % Matrix.mod
            return Matrix(res)
        else:
            n = other
            res = [[(n * self._matrix[i][j]) % Matrix.mod for j in range(self.column)] for i in range(self.row)]
            return Matrix(res)

    def __pow__(self, m):
        if self.column != self.row:
            raise Exception("the size of row must be the same as that of column")

        n = self.row
        res = Matrix([[int(i == j) for i in range(n)] for j in range(n)])
        base = self
        while m:
            if m % 2 == 1:
                res = res * base
            base = base * base
            m //= 2
        return res

    def __str__(self):
        res = []
        for i in range(self.row):
            for j in range(self.column):
                res.append(str(self._matrix[i][j]))
                res.append(" ")
            res.append("\n")
        res = res[:len(res) - 1]
        return "".join(res)

# ----------------- 原题核心逻辑：判断点集是否可以由两条直线覆盖 -----------------

def solve(n, X, Y):
    if n <= 3:
        return True

    def check(i, j, k):
        return (Y[k] - Y[j]) * (X[j] - X[i]) == (Y[j] - Y[i]) * (X[k] - X[j])

    # 以 (0,1) 为第一条直线的候选
    a, b = -1, -1
    for i in range(n):
        if not check(0, 1, i):
            if a == -1:
                a = i
            elif b == -1:
                b = i
            else:
                if not check(a, i, b):
                    break
    else:
        return True

    # 以 (2,1) 为第一条直线的候选
    a, b = -1, -1
    for i in range(n):
        if not check(2, 1, i):
            if a == -1:
                a = i
            elif b == -1:
                b = i
            else:
                if not check(a, i, b):
                    break
    else:
        return True

    # 以 (0,2) 为第一条直线的候选
    a, b = -1, -1
    for i in range(n):
        if not check(0, 2, i):
            if a == -1:
                a = i
            elif b == -1:
                b = i
            else:
                if not check(a, i, b):
                    break
    else:
        return True

    return False

# ----------------- main(n)：生成测试数据并运行 -----------------

def main(n):
    """
    生成规模为 n 的随机点集，调用 solve 并输出结果。
    测试数据生成策略：
      - 一半概率生成“YES”样例（随机两条直线上的点，允许部分重合）
      - 一半概率生成“随机”样例（均匀随机点）
    """
    # 为了可重复性，可以固定种子；如需完全随机，可注释掉下一行
    random.seed(0)

    X = [0] * n
    Y = [0] * n

    if n <= 3:
        # 任意生成 n 个点即可
        for i in range(n):
            X[i] = random.randint(-10**6, 10**6)
            Y[i] = random.randint(-10**6, 10**6)
    else:
        if random.random() < 0.5:
            # 构造必然为 YES 的样例：两条随机直线上的点
            # 直线1: y = a1 * x + b1
            # 直线2: y = a2 * x + b2，且尽量不同
            a1 = random.randint(-5, 5)
            b1 = random.randint(-10, 10)
            a2 = a1
            b2 = b1
            while a2 == a1 and b2 == b1:
                a2 = random.randint(-5, 5)
                b2 = random.randint(-10, 10)

            for i in range(n):
                if i % 2 == 0:
                    x = random.randint(-1000, 1000)
                    y = a1 * x + b1
                else:
                    x = random.randint(-1000, 1000)
                    y = a2 * x + b2
                X[i] = x
                Y[i] = y
        else:
            # 完全随机样例，可能是 YES 也可能是 NO
            for i in range(n):
                X[i] = random.randint(-10**6, 10**6)
                Y[i] = random.randint(-10**6, 10**6)

    ans = solve(n, X, Y)
    print("YES" if ans else "NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)