def main(n):
    MOD = 1000000007
    lines = max(1, n)  # ensure at least 1 line

    # deterministic generation of input structure:
    # first line: number of lines
    # next 'lines' lines: characters, alternating 'f' and 's'
    chars = ['f' if i % 2 == 0 else 's' for i in range(lines)]

    dp = [0] * lines
    f = 1
    dp[0] = 1

    for i in range(lines):
        char_in = chars[i]
        if char_in == 'f':
            f += 1
        else:
            for j in range(1, f):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

    print(dp[f - 1])


if __name__ == "__main__":
    # example deterministic run; adjust n as needed for experiments
    main(10)