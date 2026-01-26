def main(n):
    # Interpret n as the size of each color array, capped at 200
    size = max(1, min(200, n))

    # Deterministically generate R, G, B based on size
    R = [(i * 2 + 1) % 1000 for i in range(size)]
    G = [(i * 3 + 2) % 1000 for i in range(size)]
    B = [(i * 5 + 3) % 1000 for i in range(size)]

    a = len(R)
    b = len(G)
    c = len(B)

    # Cap lengths at 200 to respect original dp dimensions
    a = min(a, 200)
    b = min(b, 200)
    c = min(c, 200)
    R = R[:a]
    G = G[:b]
    B = B[:c]

    dp = [[[0 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]

    R.sort()
    G.sort()
    B.sort()

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + R[i - 1] * B[k - 1])

    # print(dp[a][b][c])
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(100)