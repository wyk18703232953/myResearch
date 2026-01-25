def main(n):
    import math

    rgb = 'RGB'

    # Deterministic generation of test cases based on n
    # We will create t = n test cases
    t = n
    answers = []

    for query in range(t):
        # For each test case, define k and string s deterministically from n and query index
        length = max(1, n + query)  # ensure length >= 1
        k = max(1, min(length, (query % length) + 1))  # 1 <= k <= length

        # Generate a deterministic RGB string of given length
        s = ''.join(rgb[(i + query) % 3] for i in range(length))

        # Core logic from original program starts here
        n_local = length
        ans = math.inf
        for start in range(3):
            dp = [0 for _ in range(n_local + 1)]
            for i in range(n_local):
                cur = rgb[(start + i) % len(rgb)]
                dp[i + 1] = dp[i] + int(s[i] != cur)
            for i in range(n_local - k + 1):
                ans = min(ans, dp[i + k] - dp[i])
        answers.append(ans)

    # Output all answers, one per line, matching original behavior over multiple test cases
    for ans in answers:
        print(ans)


if __name__ == "__main__":
    # Example call with a chosen scale n
    main(5)