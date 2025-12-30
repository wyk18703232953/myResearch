import random
import sys


def main(n: int):
    # 生成测试数据：n 行 m 列，以及网格边权 A、B
    # 可根据需要修改 m、k 的生成方式
    m = max(1, n)              # 简单设为与 n 同规模
    k = random.randint(1, 2*n)  # 随机路径长度（偶数步时才有解）

    # A[i][j] 表示从 (i, j-1) 向右到 (i, j) 的边权，尺寸 n x m
    # B[i][j] 表示从 (i-1, j) 向下到 (i, j) 的边权，尺寸 n x m
    # 原代码中输入格式是：
    #   n 行，每行 m-1 个数 -> 右边的边权
    #   n-1 行，每行 m 个数 -> 下边的边权
    # 这里直接随机生成：
    A = [[0] * m for _ in range(n)]
    B = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(1, m):
            A[i][j] = random.randint(1, 10)
    for i in range(1, n):
        for j in range(m):
            B[i][j] = random.randint(1, 10)

    if k % 2:
        ans = [[-1] * m for _ in range(n)]
        for a in ans:
            print(*a)
        return

    ans = [[0] * m for _ in range(n)]
    lim = k // 2
    dp = [[[float("inf")] * (lim + 1) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for step in range(1, lim + 1):
        for i in range(n):
            for j in range(m):
                val = dp[i][j][step]
                # 上
                if i:
                    cand = dp[i - 1][j][step - 1] + B[i][j]
                    if cand < val:
                        val = cand
                # 左
                if j:
                    cand = dp[i][j - 1][step - 1] + A[i][j]
                    if cand < val:
                        val = cand
                # 下
                if i < n - 1:
                    cand = dp[i + 1][j][step - 1] + B[i + 1][j]
                    if cand < val:
                        val = cand
                # 右
                if j < m - 1:
                    cand = dp[i][j + 1][step - 1] + A[i][j + 1]
                    if cand < val:
                        val = cand
                dp[i][j][step] = val

    for i in range(n):
        for j in range(m):
            ans[i][j] = dp[i][j][lim] * 2

    for a in ans:
        print(*a)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)