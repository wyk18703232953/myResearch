def main(n):
    mod = 10**9 + 7

    # Generate deterministic input: sequence of 'f' and 's'
    # Here length of sequence is n, v[1..n]
    # Example pattern: 'f' when i is even, 's' when i is odd
    v = [None] * (n + 1)
    for i in range(1, n + 1):
        v[i] = 'f' if i % 2 == 0 else 's'

    dp = [[0] * (n + 2) for _ in range(n + 1)]

    for l in range(n + 2):
        dp[n][l] = 1

    for i in range(n - 1, 0, -1):
        curr_sum = 0
        for l in range(n):
            curr_sum += dp[i + 1][l]
            curr_sum %= mod
            if v[i] == 'f':
                dp[i][l] = dp[i + 1][l + 1]

            else:
                dp[i][l] = curr_sum

    # print(dp[1][0])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)