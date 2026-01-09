import sys

def main(n):
    # Map n to sizes of R, G, B; keep them balanced
    r = n
    g = n
    b = n

    # Deterministic data generation
    R = [(i * 2 + 1) % 1000 for i in range(1, r + 1)]
    G = [(i * 3 + 2) % 1000 for i in range(1, g + 1)]
    B = [(i * 5 + 3) % 1000 for i in range(1, b + 1)]

    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    R.insert(0, 0)
    G.insert(0, 0)
    B.insert(0, 0)
    dp[0][0][0] = 0
    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i and j and dp[i - 1][j - 1][k] != -1:
                    v = dp[i - 1][j - 1][k] + R[i] * G[j]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v
                if k and j and dp[i][j - 1][k - 1] != -1:
                    v = dp[i][j - 1][k - 1] + B[k] * G[j]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v
                if i and k and dp[i - 1][j][k - 1] != -1:
                    v = dp[i - 1][j][k - 1] + R[i] * B[k]
                    if v > dp[i][j][k]:
                        dp[i][j][k] = v
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(3)