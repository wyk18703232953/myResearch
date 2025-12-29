from math import inf
import random

def solve(n, m, k, A, B):
    if k % 2:
        return [[-1] * m for _ in range(n)]

    lim = k // 2
    dp = [[[inf] * (lim + 1) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for step in range(1, lim + 1):
        for i in range(n):
            for j in range(m):
                cur = dp[i][j][step]
                if i:
                    cur = min(cur, dp[i - 1][j][step - 1] + B[i][j])
                if j:
                    cur = min(cur, dp[i][j - 1][step - 1] + A[i][j])
                if i < n - 1:
                    cur = min(cur, dp[i + 1][j][step - 1] + B[i + 1][j])
                if j < m - 1:
                    cur = min(cur, dp[i][j + 1][step - 1] + A[i][j + 1])
                dp[i][j][step] = cur

    ans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = dp[i][j][lim] * 2
    return ans


def main(n):
    # 可根据需要调整生成规则，这里令 m = n，k 为不超过 2*n 的偶数
    m = n
    if n <= 1:
        m = 1
    # 生成一个不太大的偶数步数（至少为 2，若可能）
    k = max(2, (n // 2) * 2)

    # 随机生成边权，范围 1~10
    # A[i][j] 是从 (i, j-1) 到 (i, j) 的边权（j>=1 时有意义）
    A = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(1, m):
            A[i][j] = random.randint(1, 10)

    # B[i][j] 是从 (i-1, j) 到 (i, j) 的边权（i>=1 时有意义）
    B = [[0] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(m):
            B[i][j] = random.randint(1, 10)

    ans = solve(n, m, k, A, B)
    for row in ans:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)