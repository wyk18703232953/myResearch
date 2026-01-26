def main(n):
    # Deterministically generate input of size n
    # Original input: integer n and list a of length n
    # Here we generate a[i] = (i % 3) + 1 to create some patterns
    a = [(i % 3) + 1 for i in range(n)]

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
                    break
                dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k + 1][j])
    # print(dp2[0][n - 1])
    pass
if __name__ == "__main__":
    main(10)