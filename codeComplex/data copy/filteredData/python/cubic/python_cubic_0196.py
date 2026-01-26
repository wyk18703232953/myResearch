def main(n):
    # Generate deterministic input of size n
    # Original input:
    # n
    # a1 a2 ... an
    # Here we generate a[i] = (i % 3 != 0) * (i % 5)
    a = [(i % 3 != 0) * (i % 5) for i in range(n)]
    ans = [n]
    dp1 = [[0] * n for _ in range(n)]
    dp2 = [[n] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp1[i][i] = a[i]
        dp2[i][i] = 1
        for j in range(i + 1, n):
            for k in range(i, j):
                if dp1[i][k] == dp1[k + 1][j] != 0:
                    dp1[i][j] = dp1[i][k] + 1
                    dp2[i][j] = 1
                if dp2[i][j] > dp2[i][k] + dp2[k + 1][j]:
                    dp2[i][j] = dp2[i][k] + dp2[k + 1][j]
    # Return the result instead of printing, for deterministic experiments
    return dp2[0][n - 1]


if __name__ == "__main__":
    # Example fixed-scale call for experimentation
    result = main(10)
    # print(result)
    pass