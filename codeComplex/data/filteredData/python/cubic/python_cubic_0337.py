from collections import Counter
import random

mod = 998244353

def main(n: int) -> int:
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里生成 [0, 10^6] 范围内的随机整数，可按需要修改
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 2. 原始逻辑开始
    d = Counter(a)
    d[0] = 0
    b = list(d.items())
    b.sort()
    m = len(b)
    ba = [0] * m
    cn = [0] * (m + 1)
    k = h = 0

    for i, x in enumerate(b):
        while h < m and x[0] >= b[h][0] * 2:
            h += 1
        ba[i] = h - 1
        while k < m and x[0] * 2 > b[k][0]:
            k += 1
        cn[k] += x[1]

    for i in range(m):
        cn[i + 1] += cn[i]

    dp = [0] * m
    dp[0] = 1
    b_counts = [x[1] for x in b]  # 原代码中重写的 b

    for i in range(n):
        ndp = [0] * m
        for j in range(1, m):
            if cn[j] >= i - 1:
                ndp[j] = dp[j] * (cn[j] - i + 1) % mod
            dp[j] += dp[j - 1]
            if dp[j] >= mod:
                dp[j] -= mod

        for j in range(1, m):
            ndp[j] += dp[ba[j]] * b_counts[j]
            ndp[j] %= mod

        dp = ndp

    ans = sum(dp) % mod
    return ans

# 示例调用（提交到评测时可删除或注释）
if __name__ == "__main__":
    print(main(10))