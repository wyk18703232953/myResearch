def solve(mat1: list, mat2: list, K: int) -> list:
    if K % 2 == 1:
        res = [[-1] * n for _ in range(m)]
    else:
        # dp[i][j][k]为从任意地方走到(i, j)且只走k步的最小无聊数
        dp = [[[-1] * (K // 2 + 1) for _ in range(n)] for _ in range(m)]
        for k in range(K // 2 + 1):
            for i in range(m):
                for j in range(n):
                    if k == 0:
                        dp[i][j][k] = 0
                    else:
                        if i > 0 and (dp[i][j][k] == -1 or dp[i - 1][j][k - 1] + mat2[i - 1][j] < dp[i][j][k]):
                            dp[i][j][k] = dp[i - 1][j][k - 1] + mat2[i - 1][j]
                        if i < m - 1 and (dp[i][j][k] == -1 or dp[i + 1][j][k - 1] + mat2[i][j] < dp[i][j][k]):
                            dp[i][j][k] = dp[i + 1][j][k - 1] + mat2[i][j]
                        if j > 0 and (dp[i][j][k] == -1 or dp[i][j - 1][k - 1] + mat1[i][j - 1] < dp[i][j][k]):
                            dp[i][j][k] = dp[i][j - 1][k - 1] + mat1[i][j - 1]
                        if j < n - 1 and (dp[i][j][k] == -1 or dp[i][j + 1][k - 1] + mat1[i][j] < dp[i][j][k]):
                            dp[i][j][k] = dp[i][j + 1][k - 1] + mat1[i][j]
        res = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2 * dp[i][j][-1]
    for i in range(m):
        for j in range(n):
            if j < n - 1:
                print(res[i][j], end = ' ')
            else:
                print(res[i][j])
    return
                        


m, n, K = map(int, input().split())
mat1 = []
mat2 = []
for _ in range(m):
    mat1.append(list(map(int, input().split())))
for _ in range(m - 1):
    mat2.append(list(map(int, input().split())))
solve(mat1, mat2, K)
