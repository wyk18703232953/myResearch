def main(n):
    # 映射规模含义：
    # n -> 网格为 n x n，k 为与 n 相关的偶数步数（确保有意义的计算）
    m = n
    if n <= 1:
        k = 2

    else:
        k = 2 * ((n // 2) + 1)

    # 构造 left: n 行 m-1 列的边权
    left = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            # 确定性构造：与坐标相关
            row.append(1 + (i + j) % 7)
        left.append(row)

    # 构造 right: n-1 行 m 列的边权
    right = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append(1 + (i * 3 + j * 5) % 9)
        right.append(row)

    dp_old = [[0 for _ in range(m)] for _ in range(n)]
    if k % 2 != 0:
        for _ in range(n):
            # print(*[-1 for _ in range(m)])
            pass

    else:
        k //= 2
        for _ in range(k):
            dp = [[0 for _ in range(m)] for _ in range(n)]
            for row in range(n):
                for col in range(m):
                    t = float("inf")
                    if col > 0:
                        t = min(t, dp_old[row][col - 1] + 2 * left[row][col - 1])
                    if col < m - 1:
                        t = min(t, dp_old[row][col + 1] + 2 * left[row][col])
                    if row > 0:
                        t = min(t, dp_old[row - 1][col] + 2 * right[row - 1][col])
                    if row < n - 1:
                        t = min(t, dp_old[row + 1][col] + 2 * right[row][col])
                    dp[row][col] = t
            dp_old = dp
        for i in range(n):
            # print(*dp_old[i])
            pass
if __name__ == "__main__":
    # 示例：以 n=5 运行
    main(5)