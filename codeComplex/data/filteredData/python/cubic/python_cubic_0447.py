import random

def main(n):
    # 这里将 n 作为规模参数，用来生成 N, M, K
    # 可以根据需要调整规模策略
    N = n
    M = n
    # 保证 K 为偶数（因为原逻辑中若 K 为奇数，直接输出 -1）
    K = 2 * max(1, n // 2)

    # 生成测试数据：边权为 1~10 的正整数
    HEdge = [[random.randint(1, 10) for _ in range(M - 1)] for _ in range(N)]
    VEdge = [[random.randint(1, 10) for _ in range(M)] for _ in range(N - 1)]

    if K % 2:
        for _ in range(N):
            print(*[-1] * M)
        return

    INF = 10 ** 9
    half = K // 2
    dp = [[[0] * M for _ in range(N)] for _ in range(half + 1)]

    for step in range(1, half + 1):
        for i in range(N):
            for j in range(M):
                val1 = val2 = val3 = val4 = INF
                if i > 0:
                    val1 = dp[step - 1][i - 1][j] + VEdge[i - 1][j]
                if i < N - 1:
                    val2 = dp[step - 1][i + 1][j] + VEdge[i][j]
                if j > 0:
                    val3 = dp[step - 1][i][j - 1] + HEdge[i][j - 1]
                if j < M - 1:
                    val4 = dp[step - 1][i][j + 1] + HEdge[i][j]
                dp[step][i][j] = min(val1, val2, val3, val4)

    for row in dp[half]:
        print(*[v * 2 for v in row])


if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)