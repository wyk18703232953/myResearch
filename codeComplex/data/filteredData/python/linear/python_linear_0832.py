def main(n):
    # Interpret n as both:
    # - number of test cases q
    # - base length for each string; grow slightly with test index
    q = n if n > 0 else 1
    results = []
    for t in range(q):
        length = max(1, n + t)  # ensure positive length, vary by t
        k = max(1, length // 2)  # window size based on length
        # Deterministic rgb string generation using a simple periodic pattern
        pattern = "RGB"
        rgb = "".join(pattern[(i + t) % 3] for i in range(length))
        # Original algorithm logic
        dp = [0] * 3
        dp[0] = [0] * (length + 1)
        dp[1] = [0] * (length + 1)
        dp[2] = [0] * (length + 1)
        for i in range(0, length):
            if rgb[i] == 'R':
                dp[0][i + 1] = dp[2][i]
                dp[1][i + 1] = dp[0][i] + 1
                dp[2][i + 1] = dp[1][i] + 1
            if rgb[i] == 'G':
                dp[0][i + 1] = dp[2][i] + 1
                dp[1][i + 1] = dp[0][i]
                dp[2][i + 1] = dp[1][i] + 1
            if rgb[i] == 'B':
                dp[0][i + 1] = dp[2][i] + 1
                dp[1][i + 1] = dp[0][i] + 1
                dp[2][i + 1] = dp[1][i]
        repl = k
        dif = k % 3
        for j in range(3):
            for i in range(1, length - k + 2):
                repl = min(repl, -dp[j][i - 1] + dp[(j + dif) % 3][i + k - 1])
        results.append(repl)
    # For experiment usage: return results instead of printing inside
    return results


if __name__ == "__main__":
    # Example deterministic call; users can change n here for experiments
    out = main(5)
    for v in out:
        # print(v)
        pass