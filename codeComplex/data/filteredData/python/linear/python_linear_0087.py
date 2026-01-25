def main(n):
    # Generate deterministic test data based on n
    # We need pairs (a, b) with 0 <= a < 1_000_007
    # Ensure a >= 1 so that indexing dp[i - majak[i] - 1] is safe
    # We'll spread a values and simple b values deterministically

    max_index = 1000007
    # Safe lower bound for a so that (a - b - 1) >= 0 for our generated b
    # We will ensure b is small (0..4), so starting from 10 is safe
    start_a = 10
    if n <= 0:
        # Edge case: no pairs
        print(0)
        return

    pairs = []
    # Step size to spread 'a' values within bounds
    step = max((max_index - start_a - 1) // max(n, 1), 1)
    for i in range(n):
        a = start_a + i * step
        if a >= max_index:
            a = max_index - 1
        # Deterministic small b to avoid negative index
        b = (i % 5)  # 0..4
        # Ensure a - b - 1 >= 0 (always true with start_a=10 and small b)
        pairs.append((a, b))

    dp = [0] * max_index
    majak = [0] * max_index

    q = max_index
    for a, b in pairs:
        if a < q:
            q = a
        majak[a] = b

    if q >= max_index:
        # No valid a assigned; by construction this shouldn't happen, but guard anyway
        print(n)
        return

    dp[q] = 1
    ma = 1
    # The original loop goes to 1_000_003 inclusive with step 1
    upper_limit = 1000003
    for i in range(q + 1, upper_limit + 1):
        if majak[i] == 0:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - majak[i] - 1] + 1
            if dp[i] > ma:
                ma = dp[i]

    print(n - ma)


if __name__ == "__main__":
    # Example deterministic call
    main(10)