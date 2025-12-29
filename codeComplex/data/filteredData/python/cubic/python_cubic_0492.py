import random

def main(n):
    # 生成规模：
    # n: 行数
    # m: 列数 (这里设为 n，也可以按需调整为其他函数关系)
    # k: 步数 (这里示例设为一个偶数，防止全为 -1 的情况)
    m = n
    # k 不能太大，否则 O(n*m*k) 复杂度过高；这里设为与 n 同阶
    k = 2 * max(1, n // 2)

    # 生成测试数据：
    # a: n x (m-1)，水平方向边权
    # b: (n-1) x m，垂直方向边权
    # 权值随机在 1..9 之间
    if m == 1:
        # 特殊情况：只有一列，a 数组没列
        a = [[0] * 0 for _ in range(n)]
    else:
        a = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]

    if n == 1:
        # 特殊情况：只有一行，b 数组没行
        b = [[0] * m for _ in range(0)]
    else:
        b = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # ---- 原始逻辑开始 ----
    if k % 2 == 1:
        # 输出 n 行，每行 m 个 -1
        for _ in range(n):
            print(*([-1] * m))
        return

    k //= 2
    INF = 10 ** 18
    dp = [[[INF] * (k + 1) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for v in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j][v] = min(dp[i][j][v],
                                      dp[i - 1][j][v - 1] + b[i - 1][j])
                if i < n - 1:
                    dp[i][j][v] = min(dp[i][j][v],
                                      dp[i + 1][j][v - 1] + b[i][j])
                if j > 0:
                    dp[i][j][v] = min(dp[i][j][v],
                                      dp[i][j - 1][v - 1] + a[i][j - 1])
                if j < m - 1:
                    dp[i][j][v] = min(dp[i][j][v],
                                      dp[i][j + 1][v - 1] + a[i][j])

    for i in range(n):
        row = []
        for j in range(m):
            row.append(dp[i][j][k] * 2)
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)