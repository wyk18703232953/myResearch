def main():
    N, M, K = map(int, input().split())
    HEdge = [list(map(int, input().split())) for _ in range(N)]
    VEdge = [list(map(int, input().split())) for _ in range(N - 1)]
    if K % 2:
        for i in range(N):
            print(*[-1] * M)
        return
    dp = [[[0] * M for _ in range(N)] for _ in range(K // 2 + 1)]
    for i in range(1, K // 2 + 1):
        for j in range(N):
            for k in range(M):
                Val1 = Val2 = Val3 = Val4 = 10 ** 9
                if j > 0:
                    Val1 = dp[i - 1][j - 1][k] + VEdge[j - 1][k]
                if j < N - 1:
                    Val2 = dp[i - 1][j + 1][k] + VEdge[j][k]
                if k > 0:
                    Val3 = dp[i - 1][j][k - 1] + HEdge[j][k - 1]
                if k < M - 1:
                    Val4 = dp[i - 1][j][k + 1] + HEdge[j][k]
                dp[i][j][k] = min(Val1, Val2, Val3, Val4)
    for i in dp[K // 2]:
        print(*list(map(lambda x: x * 2, i)))

if __name__ == '__main__':
    main()