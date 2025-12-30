import random

def main(n):
    # 生成规模为 n 的测试数据
    # 为保证 dp 维度不越界，n 最大不超过 200
    n = min(n, 200)
    n1 = n2 = n3 = n

    # 生成随机测试数据（可根据需要修改生成规则）
    ar = [random.randint(-1000, 1000) for _ in range(n1)]
    br = [random.randint(-1000, 1000) for _ in range(n2)]
    cr = [random.randint(-1000, 1000) for _ in range(n3)]

    ar.sort()
    br.sort()
    cr.sort()

    # dp[i][j][k]：使用前 i 个 ar、前 j 个 br、前 k 个 cr 能取得的最大和
    dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + ar[i - 1] * br[j - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + ar[i - 1] * cr[k - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + br[j - 1] * cr[k - 1])

    # 输出最终结果
    print(dp[n1][n2][n3])


if __name__ == "__main__":
    # 示例：调用 main，规模设为 5
    main(5)