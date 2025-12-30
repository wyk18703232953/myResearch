import random

def main(n):
    # 生成规模参数
    # 为了可运行，这里将 m 与 n 同规模，k 设置为一个与 n 相关的偶数步数
    m = n
    # k 至少为 2，且为偶数（原算法只在 k 为偶数时有意义）
    k = max(2, 2 * (n // 2 + 1))

    # 生成测试数据：边权为 1~10 的随机整数
    # lr[i][j]：格点 (i,j) 与 (i,j+1) 的边权，大小 n x (m-1)
    lr = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    # ud[i][j]：格点 (i,j) 与 (i+1,j) 的边权，大小 (n-1) x m
    ud = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 原逻辑
    if k % 2:
        arr = [-1] * m
        for _ in range(n):
            print(*arr)
        return

    kk = k // 2
    INF = 10 ** 10
    dp = [[[INF] * (kk + 1) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j][z] = min(dp[i][j][z], dp[i - 1][j][z - 1] + ud[i - 1][j])
                if i < n - 1:
                    dp[i][j][z] = min(dp[i][j][z], dp[i + 1][j][z - 1] + ud[i][j])
                if j > 0:
                    dp[i][j][z] = min(dp[i][j][z], dp[i][j - 1][z - 1] + lr[i][j - 1])
                if j < m - 1:
                    dp[i][j][z] = min(dp[i][j][z], dp[i][j + 1][z - 1] + lr[i][j])

    ans = [[dp[i][j][kk] * 2 for j in range(m)] for i in range(n)]
    for i in range(n):
        print(*ans[i])


if __name__ == "__main__":
    # 示例：调用 main(4)，可根据需要修改 n
    main(4)