import random

def main(n):
    # 生成规模参数：n行，m列，步数k
    # 这里简单设定 m = n，k = 2*n（可按需要调整）
    m = n
    k = 2 * n  # 保证为偶数；如需测试奇数情况，可改成 2*n+1

    # 生成测试数据 A, B
    # A: n 行，每行 m-1 个数（水平边权）
    # B: n-1 行，每行 m 个数（垂直边权）
    max_w = 10  # 权值上限，可调整
    A = [[random.randint(1, max_w) for _ in range(m - 1)] for _ in range(n)]
    B = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    if k % 2 != 0:
        # 原题要求：若 k 为奇数，输出全 -1
        for _ in range(n):
            print(*([-1] * m))
        return

    # 按原逻辑进行 DP 计算
    INF = 10 ** 9
    half = k // 2
    DP = [[[INF for _ in range(m)] for _ in range(n)] for _ in range(half)]

    # 初始化 DP[0]，根据相邻边权
    for i in range(n):
        for j in range(m - 1):
            w = A[i][j]
            DP[0][i][j] = min(DP[0][i][j], w)
            DP[0][i][j + 1] = min(DP[0][i][j + 1], w)

    for i in range(n - 1):
        for j in range(m):
            w = B[i][j]
            DP[0][i][j] = min(DP[0][i][j], w)
            DP[0][i + 1][j] = min(DP[0][i + 1][j], w)

    # 迭代扩展步数
    for k1 in range(1, half):
        for i in range(n):
            for j in range(m):
                cur = DP[k1][i][j]
                if i > 0:
                    cur = min(cur, B[i - 1][j] + DP[k1 - 1][i - 1][j])
                if j > 0:
                    cur = min(cur, A[i][j - 1] + DP[k1 - 1][i][j - 1])
                if i < n - 1:
                    cur = min(cur, B[i][j] + DP[k1 - 1][i + 1][j])
                if j < m - 1:
                    cur = min(cur, A[i][j] + DP[k1 - 1][i][j + 1])
                DP[k1][i][j] = cur

    # 输出结果（总步数为 k，因此乘以 2）
    for row in DP[half - 1]:
        ans = [v * 2 for v in row]
        print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)