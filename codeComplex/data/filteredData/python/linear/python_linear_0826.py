def main(n):
    import math

    # Deterministic data generation for time complexity experiments
    # Map n to:
    # - T: number of test cases
    # - For each test case i (0-based):
    #   n_i: length of string
    #   k_i: window size
    #   s_i: string of length n_i consisting of 'R', 'G', 'B' in a fixed pattern

    rgb = 'RGB'

    # Ensure n is at least 1
    if n <= 0:
        return

    T = n  # number of test cases equals n
    results = []

    for t in range(T):
        # Define n_i to grow with t so overall size scales roughly O(n^2)
        # This makes the total processed characters ~ n^2/2 for complexity experiments
        ni = t + 1

        # Define k_i deterministically: between 1 and ni, cycling pattern
        if ni == 0:
            ki = 1

        else:
            ki = (t % ni) + 1

        # Build s_i deterministically using RGB pattern with a phase shift depending on t
        s_chars = []
        shift = t % 3
        for i in range(ni):
            s_chars.append(rgb[(i + shift) % 3])
        s = ''.join(s_chars)

        # Core algorithm from original code
        ans = math.inf
        for start in range(3):
            dp = [0 for _ in range(ni + 1)]
            for i in range(ni):
                cur = rgb[(start + i) % len(rgb)]
                dp[i + 1] = dp[i] + int(s[i] != cur)
            for i in range(ni - ki + 1):
                ans = min(ans, dp[i + ki] - dp[i])

        results.append(ans)

    # To preserve original behavior of printing per test case
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(5)