def main(n):
    """
    将原程序改为无 input() 版本，n 为规模参数。
    这里根据 n 构造一组自洽的测试数据：
    - 令 m = n
    - 令 k = 2*n（可根据需要自行调整）
    - row, col 中的权值用简单的公式生成（如 i+j），确保为正数
    """
    import sys

    # 生成测试数据
    m = n
    k = 2 * n  # 原程序要求整数 k，可自行调整规模关系

    INF = 10**6 + 2

    # row: n 行，每行 m+2 列，首尾为 INF，中间为权值
    row = []
    for i in range(n):
        # 中间 m 个值的示例生成方式：i+j
        middle = [i + j + 1 for j in range(m)]
        row.append([INF] + middle + [INF])

    # col: n+1 行，每行 m+2 列，首尾为 INF，中间为权值
    col = [[INF] * (m + 2)]
    for i in range(n - 1):
        middle = [i + j + 2 for j in range(m)]
        col.append([INF] + middle + [INF])
    col.append([INF] * (m + 2))

    # 原逻辑开始
    if k % 2:
        dp = [[-1 for _ in range(m)] for _ in range(n)]
    else:
        k //= 2
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = 2 * min(
                    row[i][j],
                    row[i][j + 1],
                    col[i][j + 1],
                    col[i + 1][j + 1],
                )
        k -= 1
        while k:
            k -= 1
            temp = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    ck = dp[i][j] * 8
                    if i >= 1:
                        ck = min(ck, dp[i - 1][j] + 2 * col[i][j + 1])
                    if i < n - 1:
                        ck = min(ck, dp[i + 1][j] + 2 * col[i + 1][j + 1])
                    if j >= 1:
                        ck = min(ck, dp[i][j - 1] + 2 * row[i][j])
                    if j < m - 1:
                        ck = min(ck, dp[i][j + 1] + 2 * row[i][j + 1])
                    temp[i][j] = ck
            dp = temp

    # 输出结果
    for i in dp:
        print(*i)


if __name__ == "__main__":
    # 示例：运行 main(3)
    main(3)