def main(n):
    # 自行设定 m、k 的生成规则，这里示例为：
    # m = n，k = 4（偶数，便于演示），也可按需修改为其他策略
    m = n
    k = 4

    # 生成测试数据：
    # rows: n 行 m-1 列（每个点和右边点之间的边权）
    # cols: n-1 行 m 列（每个点和下边点之间的边权）
    # 为简单起见，使用从 1 开始的顺序整数作为权值
    rows = []
    val = 1
    for _ in range(n):
        row = []
        for _ in range(m - 1):
            row.append(val)
            val += 1
        rows.append(row)

    cols = []
    for _ in range(n - 1):
        col = []
        for _ in range(m):
            col.append(val)
            val += 1
        cols.append(col)

    def solve():
        if k % 2 == 1:
            return [[-1] * m for _ in range(n)]
        half = k // 2
        dp = [[[0] * (half + 1) for _ in range(m)] for _ in range(n)]
        for step in range(1, half + 1):
            for i in range(n):
                for j in range(m):
                    candidates = []
                    # left
                    if j > 0:
                        candidates.append(dp[i][j - 1][step - 1] + 2 * rows[i][j - 1])
                    # right
                    if j < m - 1:
                        candidates.append(dp[i][j + 1][step - 1] + 2 * rows[i][j])
                    # up
                    if i > 0:
                        candidates.append(dp[i - 1][j][step - 1] + 2 * cols[i - 1][j])
                    # down
                    if i < n - 1:
                        candidates.append(dp[i + 1][j][step - 1] + 2 * cols[i][j])
                    dp[i][j][step] = min(candidates)
        return [[dp[i][j][half] for j in range(m)] for i in range(n)]

    ans = solve()
    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值
    main(3)