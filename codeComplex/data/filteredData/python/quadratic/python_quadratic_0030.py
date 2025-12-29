import random

mod = 1000000007
f = []


def fact(n, m):
    global f
    f = [1 for _ in range(n + 1)]
    f[0] = 1
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
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m


def solve_C(n):
    # 生成测试数据：长度为 n 的指令序列，每个为 'f' 或 's'
    s = []
    mxI = 0
    for _ in range(n):
        c = 'f' if random.randint(0, 1) == 0 else 's'
        s.append(c)
        if c == 'f':
            mxI += 1

    dp = [[0 for _ in range(mxI + 1)] for _ in range(n)]
    dp[0][0] = 1
    preSum = [1 for _ in range(mxI + 1)]

    for i in range(1, n):
        pre = 0
        for j in range(mxI + 1):
            if s[i - 1] == 'f':
                dp[i][j] = dp[i - 1][j - 1] % mod if j - 1 >= 0 else 0
            else:
                dp[i][j] = (preSum[mxI] % mod - (pre if j != 0 else 0) % mod) % mod
            pre = preSum[j]
            preSum[j] = ((preSum[j - 1] if j != 0 else 0) % mod + dp[i][j] % mod) % mod

    return preSum[mxI] % mod


def solve_D(n):
    # 为 D 生成测试数据：
    # n 行，每行是长度 m 的 '0'/'1' 字符串，且总共有 k 个 '1'
    # 为了简单，令 m = n + 5，k = min(n, 总 1 的个数上限)
    m = max(1, n + 5)
    # 控制总的 '1' 数量，避免太大
    total_ones = max(0, min(n * m // 3, n))
    k = min(n, total_ones)

    w = [['0' for _ in range(m)] for _ in range(n)]
    ones_left = total_ones
    for i in range(n):
        # 本行的 1 数目
        if i == n - 1:
            cnt = ones_left
        else:
            # 随机分配，但不超过本行容量
            max_here = min(ones_left, m // 2)
            cnt = random.randint(0, max_here) if max_here > 0 else 0
        ones_left -= cnt
        pos = random.sample(range(m), cnt) if cnt > 0 else []
        for p in pos:
            w[i][p] = '1'
    # 转为字符列表
    w = [list(''.join(row)) for row in w]

    mn = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(k + 1):
            c = 0
            st, en = -1, -1
            # 从左到右
            for x in range(m):
                if w[i - 1][x] == '1':
                    if c == j and st == -1:
                        st = x
                    if c < j:
                        c += 1
                    if c == j:
                        en = x
            mn[i][j] = en - st + 1 if st != -1 and en != -1 else 0

            # 从右到左
            st, en = -1, -1
            c = 0
            for x in range(m - 1, -1, -1):
                if w[i - 1][x] == '1':
                    if c == j and st == -1:
                        st = x
                    if c < j:
                        c += 1
                    if c == j:
                        en = x
            if st != -1 and en != -1:
                val = st - en + 1
                if mn[i][j] == 0:
                    mn[i][j] = val
                else:
                    mn[i][j] = min(mn[i][j], val)

    dp = [[10 ** 18 for _ in range(k + 1)] for _ in range(n + 1)]
    for j in range(k + 1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(k + 1):
            for x in range(k + 1):
                if j - x >= 0:
                    cand = dp[i - 1][j - x] + mn[i][x]
                    if cand < dp[i][j]:
                        dp[i][j] = cand

    return dp[n][k]


def main(n):
    """
    n 为规模参数：
    - 用于 C：长度为 n 的指令序列
    - 用于 D：n 行、每行长度约为 n+5 的 0/1 矩阵
    返回一个字典，包含两部分的运行结果，方便测试。
    """
    res_C = solve_C(n)
    res_D = solve_D(n)
    return {"C": res_C, "D": res_D}