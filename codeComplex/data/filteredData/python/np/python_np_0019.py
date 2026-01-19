import sys
from array import array  # noqa: F401


def generate_prob_matrix(n):
    prob = [[0.0] * n for _ in range(n)]
    if n <= 1:
        return prob
    # Deterministic generation: prob[i][j] + prob[j][i] = 1 for i != j
    for i in range(n):
        for j in range(n):
            if i == j:
                prob[i][j] = 0.0
            elif i < j:
                # Some deterministic function of (i, j, n)
                val = ((i + 1) * (j + 2)) % (n + 3)
                prob[i][j] = val / (n + 3)
            else:
                prob[i][j] = 1.0 - prob[j][i]
    return prob


def main(n):
    prob = generate_prob_matrix(n)
    full_bit = (1 << n) - 1
    dp = [0.0] * full_bit + [1.0]

    for bit in range(full_bit, 0, -1):
        popcount = len([1 for i in range(n) if (1 << i) & bit])
        if popcount == 1 or dp[bit] == 0.0:
            continue
        div = 1 / ((popcount * (popcount - 1)) >> 1)

        for i in range(n):
            if ((1 << i) & bit) == 0:
                continue
            for j in range(i + 1, n):
                if ((1 << j) & bit) == 0:
                    continue
                dp[bit - (1 << j)] += dp[bit] * prob[i][j] * div
                dp[bit - (1 << i)] += dp[bit] * prob[j][i] * div

    print(*(dp[1 << i] for i in range(n)))


if __name__ == "__main__":
    main(5)