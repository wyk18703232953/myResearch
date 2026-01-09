def main(n):
    # Interpret n as the total length of three arrays; split as evenly as possible
    if n < 0:
        n = 0
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # Deterministic data generation using simple arithmetic patterns
    Rs = [i * 2 + 1 for i in range(R)]
    Gs = [i * 3 + 2 for i in range(G)]
    Bs = [i * 5 + 3 for i in range(B)]

    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                t = 0
                if i > 0 and j > 0:
                    v = dp[i - 1][j - 1][k] + Rs[i - 1] * Gs[j - 1]
                    if v > t:
                        t = v
                if j > 0 and k > 0:
                    v = dp[i][j - 1][k - 1] + Gs[j - 1] * Bs[k - 1]
                    if v > t:
                        t = v
                if k > 0 and i > 0:
                    v = dp[i - 1][j][k - 1] + Bs[k - 1] * Rs[i - 1]
                    if v > t:
                        t = v
                dp[i][j][k] = t
                if ans < t:
                    ans = t
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)