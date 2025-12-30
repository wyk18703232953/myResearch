from functools import lru_cache
import random

mod = 10 ** 9 + 7
mod2 = 998244353

def main(n: int):
    """
    n 用来控制数据规模：
    - R, G, B 在 [1, n] 中随机
    - 每个数组元素在 [1, 10^4] 中随机
    """
    global ans, R, G, B, r, g, b, dp
    ans = 0

    # 根据 n 生成测试数据
    R = random.randint(1, n)
    G = random.randint(1, n)
    B = random.randint(1, n)

    r = [random.randint(1, 10_000) for _ in range(R)]
    g = [random.randint(1, 10_000) for _ in range(G)]
    b = [random.randint(1, 10_000) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 三维 DP 初始化为 -1
    dp = [[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    def rec(i, j, k):
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        x1 = x2 = x3 = 0
        if i < R and j < G:
            x1 = r[i] * g[j] + rec(i + 1, j + 1, k)
        if i < R and k < B:
            x2 = r[i] * b[k] + rec(i + 1, j, k + 1)
        if j < G and k < B:
            x3 = g[j] * b[k] + rec(i, j + 1, k + 1)
        dp[i][j][k] = max(x1, x2, x3)
        nonlocal ans
        ans = max(ans, dp[i][j][k])
        return dp[i][j][k]

    rec(0, 0, 0)
    print(ans)


if __name__ == "__main__":
    # 示例：规模参数 n=10，可按需修改
    main(10)