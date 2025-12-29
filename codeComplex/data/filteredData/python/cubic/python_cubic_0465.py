import math
import random

def main(n):
    # 生成规模
    # 为了保证有意义的网格，m 至少为 2
    m = max(2, n)
    # k 取偶数，且至少为 2
    k = 2 * max(1, n // 2)

    # 生成测试数据：边权为 1~10 的随机整数
    horizontal = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    vertical = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2 or max(n, m) == 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    dp = [[[0] * (k // 2 + 1) for _ in range(m)] for _ in range(n)]

    for length in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                left_path = math.inf if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = math.inf if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = math.inf if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = math.inf if i == n - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    for i in range(n):
        print(*[dp[i][j][k // 2] * 2 for j in range(m)])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)