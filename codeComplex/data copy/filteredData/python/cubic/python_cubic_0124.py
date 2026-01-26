def main(n):
    # Interpret n as:
    # length of s = n
    # length of t = n
    # number of test cases T = 3 (constant, to make it scalable with string size)
    T = 3

    # Deterministic construction of test cases
    test_cases = []
    for ti in range(T):
        # Construct s and t deterministically based on n and ti
        # s: pattern "abc..." repeated
        base = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(base[i % 26] for i in range(n))

        # t: shift s by ti and take first n characters
        t = "".join(base[(i + ti) % 26] for i in range(n))

        test_cases.append((s, t))

    # Core logic from original program, applied to generated test cases
    for ti in range(T):
        s, t = test_cases[ti]
        N = len(t)
        answered = False
        for i in range(1, N + 1):
            dp = [[0] + [-1] * i for _ in range(len(s) + 1)]
            for l, c in enumerate(s):
                for j in range(i + 1):
                    dp[l + 1][j] = dp[l][j]
                    if dp[l][j] != -1:
                        if i + dp[l][j] < N and t[i + dp[l][j]] == c:
                            dp[l + 1][j] = dp[l][j] + 1
                    if j != 0 and c == t[j - 1]:
                        if dp[l][j - 1] > dp[l + 1][j]:
                            dp[l + 1][j] = dp[l][j - 1]
            if dp[-1][i] == N - i:
                # print("YES")
                pass
                answered = True
                break
        if not answered:
            # print("NO")
            pass
if __name__ == "__main__":
    main(1000)