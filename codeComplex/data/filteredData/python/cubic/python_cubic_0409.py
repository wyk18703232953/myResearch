import random
import sys


def main(n):
    # 生成规模参数
    # n: 行数
    # 这里生成一个相对合理的 m, k
    m = max(1, n)                 # 列数，简单设为与 n 相同
    k = 2 * random.randint(1, 5)  # 必须是偶数才能有意义，这里限定为不大的偶数

    inf = float('inf')

    # 生成测试数据 A, B
    # A: n 行 m-1 列，表示水平方向的边权(从(j)到(j+1))
    # B: n-1 行 m 列，表示竖直方向的边权(从(i)到(i+1))
    # 原题里 A, B 的形状为:
    #   A: n x (m-1)
    #   B: (n-1) x m
    # 但原代码在访问时写成了 A[i][j] / A[i][j-1]，对应 m-1 列的含义：
    #   A[i][j]       对应 (i, j) -> (i, j+1) 的边
    #   A[i][j-1]     对应 (i, j) -> (i, j-1) 的边
    # 同理 B:
    #   B[i][j]       对应 (i, j) -> (i+1, j)
    #   B[i-1][j]     对应 (i, j) -> (i-1, j)
    #
    # 然而原代码在读入时写的是:
    #   for _ in range(n):
    #       A.append(list(map(int,input().split())))
    #   for _ in range(n-1):
    #       B.append(list(map(int,input().split())))
    # 说明实际输入是:
    #   A: n x m
    #   B: (n-1) x m
    # 只是用到了部分列/行。我们保持这种数据规模。

    A = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    B = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 若 k 为奇数，则无解，全为 -1
    if k % 2 == 1:
        ans = [[-1] * m for _ in range(n)]
        for row in ans:
            print(*row)
        return

    # 动态规划
    dp = [[inf] * m for _ in range(n)]
    ans = [[None] * m for _ in range(n)]

    half = k // 2
    for l in range(half + 1):
        new_dp = [[inf] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if l == 0:
                    new_dp[i][j] = 0
                    continue

                # 上
                up = B[i - 1][j] * 2 + dp[i - 1][j] if i - 1 >= 0 else inf
                # 右
                right = A[i][j] * 2 + dp[i][j + 1] if j + 1 < m else inf
                # 左
                left = A[i][j - 1] * 2 + dp[i][j - 1] if j - 1 >= 0 else inf
                # 下
                down = B[i][j] * 2 + dp[i + 1][j] if i + 1 < n else inf

                new_dp[i][j] = min(up, right, left, down)

                if l == half:
                    ans[i][j] = new_dp[i][j]
        dp = new_dp

    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)