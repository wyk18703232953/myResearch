from collections import defaultdict
import random
import math

INF = float("inf")

# Helpers (kept for structure similarity, though not all are used)
def mus(d=0):
    return defaultdict(defaultdict(d))

def ms(x, y, d=0):
    return [[d] * y for _ in range(x)]

def ar(x, d=0):
    return [d] * x

# Globals (max n will be determined from test generation)
MAXN = 500  # can be adjusted if needed
dp = ms(MAXN + 1, MAXN + 1)
dp2 = ar(MAXN + 1, INF)
arr = []


def calc_dp(l, r):
    # interval [l, r), 0-based
    assert l < r

    if l + 1 == r:
        dp[l][r] = arr[l]
        return dp[l][r]
    if dp[l][r] != 0:
        return dp[l][r]

    dp[l][r] = -1

    for i in range(l + 1, r):
        lf = calc_dp(l, i)
        rg = calc_dp(i, r)
        if lf > 0 and lf == rg:
            dp[l][r] = lf + 1
            return dp[l][r]

    return dp[l][r]


def solve(a, n):
    global arr, dp, dp2
    arr = a

    # reset dp and dp2 for current n
    for i in range(n + 1):
        dp2[i] = INF
        for j in range(n + 1):
            dp[i][j] = 0

    dp2[0] = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            v = calc_dp(i, j)
            if v > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)

    ans = dp2[n]
    return ans


def generate_test_data(n):
    # 生成规模为 n 的数组 arr
    # 可根据需求调整生成策略，这里使用随机正整数（1..3）以便产生可合并结构
    random.seed(0)
    return [random.randint(1, 3) for _ in range(n)]


def main(n):
    """
    n: 问题规模（数组长度）
    返回：solve 的结果
    """
    global MAXN, dp, dp2

    if n > MAXN:
        # 扩容全局 dp、dp2
        MAXN = n
        dp = ms(MAXN + 1, MAXN + 1)
        dp2 = ar(MAXN + 1, INF)

    arr = generate_test_data(n)
    result = solve(arr, n)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)