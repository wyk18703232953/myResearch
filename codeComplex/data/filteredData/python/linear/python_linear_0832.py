def main(n):
    # Interpret n as the length of the string for each test case
    # and also the k used in the algorithm (clamped to at least 1).
    q = 3  # fixed number of test cases for scalability in outer loop
    k = max(1, n // 2)

    # Deterministic generation of q test strings of length n over {'R','G','B'}
    base = ['R', 'G', 'B']
    rgb_list = []
    for t in range(q):
        s = [base[(i + t) % 3] for i in range(n)]
        rgb_list.append(''.join(s))

    for t in range(q):
        rgb = rgb_list[t]
        dp = [0] * 3
        dp[0] = [0] * (n + 1)
        dp[1] = [0] * (n + 1)
        dp[2] = [0] * (n + 1)
        for i in range(0, n):
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
        if n >= k:
            for j in range(3):
                for i in range(1, n - k + 2):
                    repl = min(repl, -dp[j][i - 1] + dp[(j + dif) % 3][i + k - 1])
        # print(repl)
        pass
if __name__ == "__main__":
    main(10)