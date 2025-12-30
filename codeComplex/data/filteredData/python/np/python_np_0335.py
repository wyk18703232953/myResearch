import random

INF = 10**9 + 7

def main(n):
    # 1. 根据规模 n 生成测试数据
    #    这里令 N = n，M = max(1, n)；元素取 0~100 之间的随机整数
    N = n
    M = max(1, n)
    random.seed(0)  # 固定种子便于复现
    table = [[random.randint(0, 100) for _ in range(M)] for _ in range(N)]

    # 2. 按原逻辑构造 A, B
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

    # 3. DP 与 calc 保持原逻辑
    dp = [[-1] * N for _ in range(1 << N)]

    def calc(mask, v):
        if dp[mask][v] != -1:
            return dp[mask][v]
        res = 0
        for u in range(N):
            if (mask & (1 << u)) and u != v:
                res = max(res, min(calc(mask ^ (1 << v), u), A[u][v]))
        dp[mask][v] = res
        return res

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
    # 示例：规模 n = 4
    main(4)