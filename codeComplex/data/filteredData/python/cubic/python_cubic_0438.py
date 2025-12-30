import random

def main(n):
    # 生成规模参数：
    # n: 行数
    # m: 列数（这里设为与 n 相同，也可按需调整）
    # k: 步数（设为偶数以得到有效结果）
    m = n
    k = 2 * max(1, n // 2)

    INF = 10**9

    # 生成测试数据：right 为 n 行 (m-1) 列，down 为 (n-1) 行 m 列
    # 边权随机生成 1~9
    if m > 1:
        right = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    else:
        right = [[] for _ in range(n)]  # 如果 m == 1，没有右边的边

    if n > 1:
        down = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]
    else:
        down = []  # 如果 n == 1，没有下边的边

    # 原逻辑
    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    k_half = k // 2
    dp = [[[INF for _ in range(m)] for _ in range(n)] for _ in range(k_half + 1)]

    for steps in range(k_half + 1):
        for i in range(n):
            for j in range(m):
                if steps == 0:
                    dp[steps][i][j] = 0
                    continue
                ans = INF
                if i > 0:
                    ans = min(ans, dp[steps - 1][i - 1][j] + down[i - 1][j])
                if i < n - 1:
                    ans = min(ans, dp[steps - 1][i + 1][j] + down[i][j])
                if j < m - 1:
                    ans = min(ans, dp[steps - 1][i][j + 1] + right[i][j])
                if j > 0:
                    ans = min(ans, dp[steps - 1][i][j - 1] + right[i][j - 1])
                dp[steps][i][j] = ans

    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(2 * dp[k_half][i][j]))
        print(" ".join(row))


# 示例调用：
# main(4)