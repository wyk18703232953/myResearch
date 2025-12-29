import sys
sys.setrecursionlimit(50000)


def main(n):
    """
    n: 用于生成测试数据的规模参数。
       我们在此示例中构造一个大致为 n x n 的网格，并令 k = 2 * n（保证为偶数）。
    """
    # 根据 n 构造 m, k
    m = n
    if n <= 0:
        return
    k = 2 * n  # 必须为偶数，才能有解

    # 生成测试数据：这里简单生成 1.. 的递增权重
    # s[i][j][d] 的含义保持不变：四个方向 0 上,1 右,2 下,3 左
    s = [[[-1, -1, -1, -1] for _ in range(m)] for _ in range(n)]

    # 生成水平边权：n 行，每行 m-1 个
    # 第 i 行，从左到右依次为 1,2,...,m-1
    for i in range(n):
        d = list(range(1, m))  # [1, 2, ..., m-1]
        for j in range(m - 1):
            s[i][j][1] = d[j]       # (i,j) -> (i,j+1)
            s[i][j + 1][3] = d[j]   # (i,j+1) -> (i,j)

    # 生成竖直边权：n-1 行，每行 m 个
    # 第 i 行，从上到下依次为 1,2,...,m
    for i in range(n - 1):
        d = list(range(1, m + 1))   # [1, 2, ..., m]
        for j in range(m):
            s[i][j][2] = d[j]       # (i,j) -> (i+1,j)
            s[i + 1][j][0] = d[j]   # (i+1,j) -> (i,j)

    # 按原逻辑进行计算
    if k % 2 == 1:
        for _ in range(n):
            print(*[-1 for _ in range(m)])
        return

    half = k // 2
    INF = 9999999
    dp = [[[INF for _ in range(half + 1)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for q in range(1, half + 1):
        for i in range(n):
            for j in range(m):
                cands = []
                if i > 0:
                    cands.append(dp[i - 1][j][q - 1] + s[i - 1][j][2])
                if j > 0:
                    cands.append(dp[i][j - 1][q - 1] + s[i][j - 1][1])
                if i < n - 1:
                    cands.append(dp[i + 1][j][q - 1] + s[i + 1][j][0])
                if j < m - 1:
                    cands.append(dp[i][j + 1][q - 1] + s[i][j + 1][3])
                dp[i][j][q] = min(cands)

    for i in range(n):
        for j in range(m):
            print(2 * dp[i][j][half], end=' ')
        print()


if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(4)