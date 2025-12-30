import random
from array import array  # noqa: F401


def main(n: int) -> int:
    mod = 998244353

    # 生成测试数据：k 在 [1, n^2] 范围内随机取值，至少为 1
    k = random.randint(1, max(1, n * n))

    if k == 1:
        return 0

    # 原始逻辑开始
    dp1 = [array('i', [0]) * n for _ in range(n)]
    dp2 = [array('i', [0]) * n for _ in range(n)]
    dp1[0][0] = 1

    for i in range(n - 1):
        for j in range(i + 1):
            for l in range(j + 1):
                dp2[j][0] += dp1[j][l]
                if dp2[j][0] >= mod:
                    dp2[j][0] -= mod

                idx_j = j + 1 if j == l else j
                dp2[idx_j][l + 1] += dp1[j][l]
                if dp2[idx_j][l + 1] >= mod:
                    dp2[idx_j][l + 1] -= mod

                dp1[j][l] = 0

        dp1, dp2 = dp2, dp1

    ans = 0
    for i in range(1, n + 1):
        t = (k - 1) // i
        if t == 0:
            break

        dps1 = array('i', [0]) * (t + 1)
        dps2 = array('i', [0]) * (t + 1)
        dps1[0] = 1

        for j in range(n - 1):
            upper = min(j + 1, t)
            for l in range(upper):
                dps2[0] += dps1[l]
                if dps2[0] >= mod:
                    dps2[0] -= mod

                dps2[l + 1] += dps1[l]
                if dps2[l + 1] >= mod:
                    dps2[l + 1] -= mod

                dps1[l] = 0

            dps1, dps2 = dps2, dps1

        x = sum(dp1[i - 1]) % mod
        ans = (ans + x * sum(dps1[:-1])) % mod

    return ans * 2 % mod