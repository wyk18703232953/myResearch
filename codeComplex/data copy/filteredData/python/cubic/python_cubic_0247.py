def main(n):
    # Interpret n as the size of each color array: R = G = B = n
    R = G = B = n

    # Deterministic data generation based on n
    Rs = [(i * 2 + 1) for i in range(R)]
    Gs = [(i * 3 + 2) for i in range(G)]
    Bs = [(i * 5 + 3) for i in range(B)]

    # Keep original behavior: sort in descending order
    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)

    # DP initialization
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    answer = 0

    # Core algorithm identical to original solve()
    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                if r > 0 and g > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r - 1][g - 1][b] + Rs[r - 1] * Gs[g - 1])
                if g > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r][g - 1][b - 1] + Gs[g - 1] * Bs[b - 1])
                if r > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r - 1][g][b - 1] + Rs[r - 1] * Bs[b - 1])
                if dp[r][g][b] > answer:
                    answer = dp[r][g][b]

    return answer


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    # print(main(5))
    pass