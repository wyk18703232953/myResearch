import random
import math
from collections import defaultdict as dd

mod = 1000000007

def main(n):
    # 根据规模 n 生成测试数据
    # 这里设置：
    #   m 与 n 相同，形成 n x n 网格
    #   k 与 2*n 相同，保证为偶数且能体现一定路径长度
    m = n
    k = 2 * n  # 可根据需要调整生成规则，只要保证为偶数即可

    # 生成权重矩阵：
    # h: 水平方向边权，大小 n x (m-1)
    # v: 垂直方向边权，大小 (n-1) x m
    # 边权随机生成为 1~9 的整数
    h = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    v = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 三维 DP 数组: dp[i][j][l] 表示从 (i,j) 出发走 l 步的最小代价(一边)
    dp = [[[0 for _ in range(k // 2 + 1)] for _ in range(m)] for _ in range(n)]

    def sol(n, m, k):
        for l in range(1, k // 2 + 1):
            for i in range(n):
                for j in range(m):
                    dp[i][j][l] = float("inf")
                    if j - 1 >= 0:
                        dp[i][j][l] = min(dp[i][j][l], dp[i][j - 1][l - 1] + h[i][j - 1])
                    if i - 1 >= 0:
                        dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l - 1] + v[i - 1][j])
                    if j + 1 < m:
                        dp[i][j][l] = min(dp[i][j][l], dp[i][j + 1][l - 1] + h[i][j])
                    if i + 1 < n:
                        dp[i][j][l] = min(dp[i][j][l], dp[i + 1][j][l - 1] + v[i][j])
        return dp

    if k % 2:
        for i in range(n):
            for j in range(m):
                print(-1, end=" ")
            print()
    else:
        ans = sol(n, m, k)
        for i in range(n):
            for j in range(m):
                # 原题要求往返路径总步数为 k，因此乘 2
                print(2 * ans[i][j][k // 2], end=" ")
            print()


# 示例调用（提交到评测系统时可删除或注释）
if __name__ == "__main__":
    main(3)