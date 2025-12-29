import random

def main(n):
    # 生成测试数据：n 行 n 列的网格，k 为偶数步数
    m = n
    # 设定一个与规模相关的步数（偶数），例如 2*n
    k = 2 * n
    if k % 2 == 1:
        k += 1

    # 生成边权：right 为 n x (m-1)，down 为 (n-1) x m
    # 原代码中 right[i] 和 down[i] 的长度分别是 m-1 和 m
    # 为了保持一致，生成时按此尺寸生成
    max_weight = 10
    right = []
    for _ in range(n):
        # 每行 m-1 个水平边
        row = [random.randint(1, max_weight) for _ in range(m - 1)]
        right.append(row)

    down = []
    for _ in range(n - 1):
        # 每行 m 个垂直边
        row = [random.randint(1, max_weight) for _ in range(m)]
        down.append(row)

    # 若 k 为奇数，直接输出 -1（按题意），但这里保证了 k 为偶数
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    k //= 2

    # dp[i][j][l] : 从 (i,j) 出发走 l 步的最小代价
    dp = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

    for l in range(k):
        for i in range(n):
            for j in range(m):
                dp[i][j][l + 1] = float("inf")
                if i > 0:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1],
                                          dp[i - 1][j][l] + down[i - 1][j])
                if j > 0:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1],
                                          dp[i][j - 1][l] + right[i][j - 1])
                if i < n - 1:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1],
                                          dp[i + 1][j][l] + down[i][j])
                if j < m - 1:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1],
                                          dp[i][j + 1][l] + right[i][j])

    for i in range(n):
        row_ans = []
        for j in range(m):
            row_ans.append(str(2 * dp[i][j][k]))
        print(" ".join(row_ans))


if __name__ == "__main__":
    # 示例：运行 main(4)
    main(4)