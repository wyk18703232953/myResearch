def main(n):
    import math

    rgb = 'RGB'

    # Deterministic test case generation based on n
    # We will generate t test cases; for simplicity, let t = max(1, n // 5)
    t = max(1, n // 5)
    cases = []

    for q in range(t):
        # Define string length and k based on n and q
        length = max(1, n + q)
        k = max(1, min(length, (q % length) + 1))

        # Deterministic construction of s using a simple pattern over 'RGB'
        s_chars = []
        for i in range(length):
            # Example pattern: shift by q and wrap in 'RGB'
            s_chars.append(rgb[(i + q) % 3])
        s = ''.join(s_chars)

        cases.append((length, k, s))

    # Core algorithm: unchanged logic, just driven by generated cases
    results = []
    for (length, k, s) in cases:
        ans = math.inf
        for start in range(3):
            dp = [0 for _ in range(length + 1)]
            for i in range(length):
                cur = rgb[(start + i) % len(rgb)]
                dp[i + 1] = dp[i] + int(s[i] != cur)
            for i in range(length - k + 1):
                ans = min(ans, dp[i + k] - dp[i])
        results.append(ans)

    # Output results line by line to match original behavior
    for res in results:
        print(res)


if __name__ == "__main__":
    # Example call; change n here to scale the experiment
    main(10)