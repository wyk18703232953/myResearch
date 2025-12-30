import random

mod = 998244353
f = []


def fact(n, m):
    """Precompute factorials mod m up to n."""
    global f
    f = [1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % m


def fast_mod_exp(a, b, m):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res


def inverseMod(n, m):
    return fast_mod_exp(n, m - 2, m)


def ncr(n, r, m):
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m


def solve_B(n, a, queries):
    """Core logic of original B() function."""
    q = len(queries)

    mat = [[0 for _ in range(n)] for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize diagonals
    for i in range(n):
        mat[i][i] = a[i]
        dp[i][i] = a[i]

    # Build mat: mat[i][j] = XOR over segment with original recurrence
    x = 1
    while x < n:
        j = x
        i = 0
        while j < n:
            mat[i][j] = mat[i][j - 1] ^ mat[i + 1][j]
            j += 1
            i += 1
        x += 1

    # Build dp: dp[i][j] is max over sub-structures
    x = 1
    while x < n:
        j = x
        i = 0
        while j < n:
            dp[i][j] = max(mat[i][j], dp[i][j - 1], dp[i + 1][j])
            j += 1
            i += 1
        x += 1

    # Answer queries
    res = []
    for l, r in queries:
        res.append(dp[l - 1][r - 1])
    return res


def main(n):
    """
    生成规模为 n 的测试数据并运行原 B() 逻辑。
    测试数据约定：
      - 数组 a 长度为 n，元素为 [0, 100] 之间的随机整数。
      - q 取 n（每个位置作为左端点一次）。
      - 查询 (l, r) 使得 1 <= l <= r <= n，右端点随机。
    返回值为一个列表，包含每个查询的答案。
    """
    if n <= 0:
        return []

    random.seed(0)  # 固定种子，保证可复现
    a = [random.randint(0, 100) for _ in range(n)]

    q = n
    queries = []
    for l in range(1, n + 1):
        r = random.randint(l, n)
        queries.append((l, r))

    # 调用原始逻辑
    answers = solve_B(n, a, queries)
    return answers