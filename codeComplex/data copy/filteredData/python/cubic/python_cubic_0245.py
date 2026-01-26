import heapq


def solve(R, G, B, Rs, Gs, Bs):
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)
    answer = 0
    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                if r > 0 and g > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r - 1][g - 1][b] + Rs[r - 1] * Gs[g - 1])
                if g > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r][g - 1][b - 1] + Gs[g - 1] * Bs[b - 1])
                if r > 0 and b > 0:
                    dp[r][g][b] = max(dp[r][g][b], dp[r - 1][g][b - 1] + Rs[r - 1] * Bs[b - 1])
                answer = max(answer, dp[r][g][b])
    return answer


def main(n):
    # Interpret n as the total scale; split into sizes for R, G, B.
    # Make them balanced so R + G + B ~ n and each >= 1.
    if n <= 0:
        return 0
    R = max(1, n // 3)
    G = max(1, (n - R) // 2)
    B = max(1, n - R - G)

    # Deterministic construction of arrays Rs, Gs, Bs with lengths R, G, B.
    # Values grow roughly linearly but differ per color.
    Rs = [i * 2 + 1 for i in range(1, R + 1)]
    Gs = [i * 3 + 2 for i in range(1, G + 1)]
    Bs = [i * 5 + 3 for i in range(1, B + 1)]

    return solve(R, G, B, Rs, Gs, Bs)


if __name__ == "__main__":
    # Example: run with n = 10 for a small deterministic experiment
    # print(main(10))
    pass