# Converted version: no input(), main(n) with generated test data.

MOD = 998244353

def solve(n, k):
    dp = [[0, 0, 0, 0] for _ in range(k + 3)]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][2] = 1
    dp[2][3] = 1
    newdp = [[0, 0, 0, 0] for _ in range(k + 3)]

    for _ in range(n - 1):
        for j in range(k + 1):
            newdp[j + 1][1] += dp[j][0]
            newdp[j + 1][3] += dp[j][0]
            newdp[j + 1][2] += dp[j][0]
            newdp[j][0] += dp[j][0]

            newdp[j][1] += dp[j][1]
            newdp[j + 1][3] += dp[j][1]
            newdp[j + 1][2] += dp[j][1]
            newdp[j + 1][0] += dp[j][1]

            newdp[j][1] += dp[j][2]
            newdp[j + 2][3] += dp[j][2]
            newdp[j][2] += dp[j][2]
            newdp[j][0] += dp[j][2]

            newdp[j][1] += dp[j][3]
            newdp[j][3] += dp[j][3]
            newdp[j + 2][2] += dp[j][3]
            newdp[j][0] += dp[j][3]

            # apply modulo locally to avoid overflow
            for a in range(3):
                for b in range(4):
                    newdp[a + j][b] %= MOD

        # move newdp to dp and reset newdp
        for a in range(k + 3):
            for b in range(4):
                dp[a][b] = newdp[a][b] % MOD
                newdp[a][b] = 0

    ans = sum(dp[k]) % MOD
    return ans


def main(n):
    """
    n: scale parameter.
    We generate k based on n as test data.
    For demonstration, set k = min(n, some bound).
    """
    # Example test data generation rule:
    # Ensure k is valid (k >= 0, small enough compared to n for typical tests).
    k = max(0, n // 2)

    result = solve(n, k)
    print(result)


if __name__ == "__main__":
    # Example: run main with some n for local testing.
    # In external use, caller should call main(n) directly.
    main(10)