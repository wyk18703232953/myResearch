import random

def main(n):
    # 这里将规模 n 同时作为行数和列数，并令 k 为偶数（如 4）
    # 如需不同规模，可按需修改 m、k 的生成方式
    m = n
    k = 4 if 4 <= 2 * max(n, m) else 2 * max(n, m)
    if k % 2 == 1:
        k += 1  # 保证 k 为偶数

    # 生成测试数据：边权为 1~10 的随机整数
    horizontal = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    vertical = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2 or max(n, m) == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    half = k // 2
    INF = 10**9
    dp = [[[0] * (half + 1) for _ in range(m)] for _ in range(n)]

    for length in range(1, half + 1):
        for i in range(n):
            for j in range(m):
                left_path = INF if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = INF if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = INF if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = INF if i == n - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    for i in range(n):
        print(*[dp[i][j][half] * 2 for j in range(m)])


if __name__ == "__main__":
    # 示例：调用 main(5) 运行规模为 5 的测试
    main(5)