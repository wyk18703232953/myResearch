def main(n):
    """
    n: 问题规模（玩家数量）
    功能：随机生成 n 个玩家的胜率矩阵 p[i][j] (i,j from 0..n-1)，
          然后执行原程序的 DP 逻辑并打印结果。
    """
    import random

    # 生成测试数据：p[i][j] 表示 i 打败 j 的概率
    # 保证 p[i][i] = 0, p[i][j] + p[j][i] = 1 (i != j)
    p = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = random.random()
            p[i][j] = v
            p[j][i] = 1.0 - v

    # DP 大小为 2^n
    dp = [0.0] * (1 << n)
    dp[1] = 1.0  # 初始状态：只有选手 0 存在

    # 按原代码逻辑，从子集 2 到 (1<<n)-1 迭代
    for mask in range(2, 1 << n):
        for j in range(1, n):
            if (mask >> j) & 1 == 0:
                continue
            for k in range(0, j):
                if (mask >> k) & 1 == 0:
                    continue
                # 原逻辑：
                # dp[mask] = max(dp[mask],
                #                dp[mask ^ (1 << j)] * p[k][j]
                #              + dp[mask ^ (1 << k)] * p[j][k])
                val = dp[mask ^ (1 << j)] * p[k][j] + dp[mask ^ (1 << k)] * p[j][k]
                if val > dp[mask]:
                    dp[mask] = val

    # 输出最终结果，对应原来的 print(dp[-1])
    print(dp[-1])


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(4)