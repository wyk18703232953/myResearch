import random

INF = 10 ** 9 + 7

def main(n):
    # 这里用 n 控制 N 的规模，M 也由 n 决定（可按需要修改规则）
    N = n
    M = max(1, n)  # 简单设定：M = n（至少为 1）

    # 3. 根据 n 生成测试数据 table[N][M]
    # 生成 0~1000 的随机整数，便于测试
    random.seed(0)
    table = [[random.randint(0, 1000) for _ in range(M)] for _ in range(N)]

    # 原逻辑开始
    A = [[0] * N for _ in range(N)]
    B = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            res = INF
            for k in range(M):
                res = min(res, abs(table[i][k] - table[j][k]))
            A[i][j] = res
            A[j][i] = res

            res = INF
            for k in range(M - 1):
                res = min(res, abs(table[i][k] - table[j][k + 1]))
            B[i][j] = res

    dp = [[-1] * N for _ in range(1 << N)]

    def calc(mask, v):
        if dp[mask][v] != -1:
            return dp[mask][v]
        res = 0
        for u in range(N):
            if (mask & (1 << u)) and u != v:
                res = max(res, min(calc(mask ^ (1 << v), u), A[u][v]))
        dp[mask][v] = res
        return dp[mask][v]

    ans = 0
    full_mask = (1 << N) - 1
    for i in range(N):
        dp = [[-1] * N for _ in range(1 << N)]
        for k in range(N):
            if k == i:
                dp[1 << k][k] = INF
            else:
                dp[1 << k][k] = 0
        for j in range(N):
            ans = max(ans, min(B[j][i], calc(full_mask, j)))

    print(ans)


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)