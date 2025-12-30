import random

def main(n):
    # 这里将 n 作为行数，列数 m 可与 n 相同或自定义规则
    m = n

    # 随机选择偶数步数 k（原算法要求 k 为偶数才有意义）
    # 可根据规模调整上限，这里设为 2*n 但至少为 2
    k = max(2, 2 * random.randint(1, max(1, n)))

    # 生成测试数据：
    # h: n 行，每行 m-1 个权值（横向边）
    # v: n-1 行，每行 m 个权值（纵向边）
    # 为了避免过大数，取 1~9 的正整数
    h = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    v = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    # 如果 k 为奇数，按原代码逻辑输出 -1
    if k % 2:
        for _ in range(n):
            print(" ".join("-1" for _ in range(m)))
        return

    half = k // 2
    INF = float('inf')

    # dp[x][i][j] 表示从 (i,j) 出发走 x 步的最小代价
    dp = [[[INF] * m for _ in range(n)] for _ in range(half + 1)]
    for i in range(n):
        for j in range(m):
            dp[0][i][j] = 0

    for x in range(1, half + 1):
        for i in range(n):
            for j in range(m):
                best = dp[x][i][j]
                if i != 0:
                    best = min(best, dp[x - 1][i - 1][j] + v[i - 1][j])
                if i != n - 1:
                    best = min(best, dp[x - 1][i + 1][j] + v[i][j])
                if j != 0:
                    best = min(best, dp[x - 1][i][j - 1] + h[i][j - 1])
                if j != m - 1:
                    best = min(best, dp[x - 1][i][j + 1] + h[i][j])
                dp[x][i][j] = best

    # 输出结果：2 * dp[half][i][j]
    for i in range(n):
        row = [str(2 * dp[half][i][j]) for j in range(m)]
        print(" ".join(row))


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)