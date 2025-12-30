import random

def main(n):
    # 生成测试数据：随机概率矩阵 p，p[i][i] = 0
    # p[i][j] 表示 i 打败 j 的概率
    p = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            prob = random.random()
            p[i][j] = prob
            p[j][i] = 1.0 - prob

    y = 1 << n
    dp = [[0.0] * y for _ in range(n)]
    # dp[i][mask]：在 mask 这一组人已经战斗过且还存活的情况下，
    # 最终 0 号选手获胜的概率（当前轮到 i 参与决斗）
    dp[0][y - 1] = 1.0

    for mask in range(y - 2, -1, -1):
        bit = 1
        for j in range(n):
            if not (mask & bit):  # j 不在 mask 中
                bit <<= 1
                continue
            bit2 = 1
            for k in range(n):
                if mask & bit2:  # k 已在 mask 中
                    bit2 <<= 1
                    continue
                new_mask = mask | bit2
                dp[j][mask] = max(
                    dp[j][mask],
                    dp[j][new_mask] * p[j][k] + dp[k][new_mask] * p[k][j]
                )
                bit2 <<= 1
            bit <<= 1

    ans = max(dp[i][1 << i] for i in range(n))
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：n=3
    main(3)