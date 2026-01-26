def main(n):
    # Map n to sizes of three arrays, roughly balanced
    r = n // 3
    g = (n - r) // 2
    b = n - r - g
    if r < 1:
        r = 1
    if g < 1:
        g = 1
    if b < 1:
        b = 1

    # Deterministic data generation
    R = [i % 1000 + 1 for i in range(r)]
    G = [(2 * i) % 1000 + 1 for i in range(g)]
    B = [(3 * i) % 1000 + 1 for i in range(b)]

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                val = dp[i][j][k]
                if i < r and j < g:
                    v = val + R[i] * G[j]
                    if v > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = v
                if i < r and k < b:
                    v = val + R[i] * B[k]
                    if v > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = v
                if j < g and k < b:
                    v = val + G[j] * B[k]
                    if v > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = v

    ans = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    return ans


if __name__ == "__main__":
    # Example call for complexity experiment
    n = 9
    result = main(n)
    # print(result)
    pass