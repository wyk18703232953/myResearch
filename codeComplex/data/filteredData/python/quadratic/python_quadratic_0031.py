def main(n):
    mod = 10**9 + 7
    # Deterministic generation of s-sequence of length n
    # Pattern: 'f' if i is even, 's' otherwise
    s_seq = ['f' if i % 2 == 0 else 's' for i in range(n)]

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        nx = [0] * (n + 1)
        s = s_seq[i]
        if s == 'f':
            nx[0] = 0
            for j in range(1, n + 1):
                nx[j] = dp[j - 1] % mod
        else:
            nx[n] = dp[n] % mod
            for j in reversed(range(n)):
                nx[j] = (nx[j + 1] + dp[j]) % mod
        if i != n - 1:
            dp = nx
    return sum(dp) % mod


if __name__ == "__main__":
    # Example call for experiment; adjust n as needed
    result = main(5)
    print(result)