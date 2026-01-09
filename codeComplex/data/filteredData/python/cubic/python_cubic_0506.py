def solve(mat1: list, mat2: list, K: int, m: int, n: int) -> list:
    if K % 2 == 1:
        res = [[-1] * n for _ in range(m)]

    else:
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
    return res


def main(n: int):
    # Interpret n as both dimensions m = n, number of columns n = n, and K = n (even-ified)
    m = n
    cols = n
    K = n if n % 2 == 0 else n + 1

    # mat1 has shape m x (n-1)
    if cols > 1:
        mat1 = [[(i * cols + j) % 7 + 1 for j in range(cols - 1)] for i in range(m)]

    else:
        mat1 = [[] for _ in range(m)]

    # mat2 has shape (m-1) x n
    if m > 1:
        mat2 = [[(i * cols + j) % 9 + 1 for j in range(cols)] for i in range(m - 1)]

    else:
        mat2 = []

    res = solve(mat1, mat2, K, m, cols)

    for i in range(m):
        row = res[i]
        if cols > 0:
            # print(" ".join(str(x) for x in row))
            pass

        else:
            # print()
            pass
if __name__ == "__main__":
    main(5)