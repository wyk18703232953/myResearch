from array import array
import random


def main(n: int):
    mod = 998244353

    # 根据规模 n 生成测试数据：k 可随 n 变化
    # 保证 k >= 2（因为原代码 k == 1 时直接输出 0）
    k = max(2, n)  # 简单示例：令 k = n（或根据需要调整策略）

    if k == 1:
        print(0)
        return

    # 初始化 dp1, dp2
    dp1 = [array('i', [0]) * n for _ in range(n)]
    dp2 = [array('i', [0]) * n for _ in range(n)]
    dp1[0][0] = 1

    # 第一段 DP
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
    # 第二段枚举 i
    for i in range(1, n + 1):
        t = (k - 1) // i
        if t == 0:
            break

        dps1 = array('i', [0]) * (t + 1)
        dps2 = array('i', [0]) * (t + 1)
        dps1[0] = 1

        # 内层 DP（与原代码一致）
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

    print(ans * 2 % mod)


if __name__ == "__main__":
    # 示例：可在此处指定 n 或由外部调用 main(n)
    main(5)