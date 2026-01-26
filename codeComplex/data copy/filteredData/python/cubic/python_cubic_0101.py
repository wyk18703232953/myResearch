MOD = 998244353

pop = []
p10 = []
f = [[0 for _ in range(1 << 10)] for _ in range(20)]
w = [[0 for _ in range(1 << 10)] for _ in range(20)]


def pop_count(x):
    ans = 0
    while x > 0:
        ans += x & 1
        x >>= 1
    return ans


def check(x, k):
    mask = 0
    nx = int(x)
    while nx > 0:
        mask |= 1 << (nx % 10)
        nx //= 10
    return x if pop_count(mask) <= k else 0


def prepare():
    # p10[i] = 10^i % MOD
    p10.append(1)
    for i in range(20):
        p10.append(p10[i] * 10 % MOD)

    # pop[mask] = number of set bits in mask
    for i in range(1 << 10):
        pop.append(pop_count(i))

    # DP precomputation
    w[0][0] = 1
    for i in range(1, 20):
        for mask in range(1 << 10):
            if w[i - 1][mask] == 0 and f[i - 1][mask] == 0:
                continue
            base_w = w[i - 1][mask]
            base_f = f[i - 1][mask]
            for use in range(10):
                nmask = mask | (1 << use)
                w[i][nmask] = (w[i][nmask] + base_w) % MOD
                f[i][nmask] = (
                    f[i][nmask]
                    + base_w * use * p10[i - 1]
                    + base_f
                ) % MOD


def solve(x, k):
    sx = [int(d) for d in str(x)]
    n = len(sx)
    ans = 0

    # Numbers with length < n
    for i in range(1, n):
        for use in range(1, 10):  # leading digit cannot be 0
            bit = 1 << use
            for mask in range(1 << 10):
                if pop[bit | mask] <= k:
                    ans = (
                        ans
                        + f[i - 1][mask]
                        + use * w[i - 1][mask] % MOD * p10[i - 1]
                    ) % MOD

    # Numbers with length = n, prefix less than x
    cmask = 0
    csum = 0
    for i in range(n):
        cdig = sx[i]
        for use in range(cdig):
            if i == 0 and use == 0:
                continue  # no leading zero
            nmask = cmask | (1 << use)
            for mask in range(1 << 10):
                if pop[nmask | mask] <= k:
                    prefix_val = (csum * 10 + use) % MOD
                    ans = (
                        ans
                        + f[n - i - 1][mask]
                        + prefix_val * w[n - i - 1][mask] % MOD * p10[n - i - 1]
                    ) % MOD
        cmask |= 1 << cdig
        csum = (10 * csum + cdig) % MOD

    return ans


def main(n):
    """
    规模 n 用来生成一组 (l, r, k) 测试数据：
    - 令 r 为 n 位数的最大值（全 9），即 r = 10^n - 1
    - 令 l = max(1, r // 2)，保证区间非空且规模与 r 同一量级
    - 令 k = min(10, max(1, n // 2))，位数越多，允许的不同数字越多
    返回原程序最终计算出的 ans。
    """
    prepare()

    # 生成测试数据
    if n <= 0:
        n = 1
    if n >= 18:
        n = 18  # 防止超出预处理长度 19 位（0..19）
    r = 10 ** n - 1
    l = max(1, r // 2)
    k = min(10, max(1, n // 2))

    ans = (check(r, k) + solve(r, k) - solve(l, k) + MOD) % MOD
    # print(ans)
    pass
    return ans