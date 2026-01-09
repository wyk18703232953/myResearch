def main(n):
    # Deterministic test generation:
    # We create T = n test cases.
    # For each test i (0-based):
    #   - length of s: Ls = max(1, i % max(1, n//2) + 1)
    #   - length of t: Lt = max(Ls, (i % n) + 1)
    #   - s and t are generated from a small alphabet to keep behavior similar.
    T = n if n > 0 else 1
    alphabet = "abc"
    tests = []
    for i in range(T):
        Ls = max(1, i % max(1, n // 2) + 1)
        Lt = max(Ls, (i % max(1, n)) + 1)
        s = "".join(alphabet[(i + j) % len(alphabet)] for j in range(Ls))
        t = "".join(alphabet[(i * 2 + j) % len(alphabet)] for j in range(Lt))
        tests.append((s, t))

    for ti in range(T):
        s, t = tests[ti]
        N = len(t)
        for i in range(1, N + 1):
            dp = [0] + [-1] * i
            for l, c in enumerate(s):
                for j in range(i, -1, -1):
                    tmp = dp[j]
                    if dp[j] != -1 and i + dp[j] < N and t[i + dp[j]] == c:
                        tmp = dp[j] + 1
                    if j != 0 and t[j - 1] == c:
                        tmp = max(tmp, dp[j - 1])
                    dp[j] = tmp
            if dp[i] == N - i:
                # print("YES")
                pass
                break

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)