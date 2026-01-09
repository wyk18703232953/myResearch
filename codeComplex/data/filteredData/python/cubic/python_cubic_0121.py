def problem(s, p):
    n = len(s)
    F = [[n] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        F[i][:] = F[i + 1]
        F[i][ord(s[i]) - 97] = i

    def interleaving(l, r):
        dp = [-1] + [n] * len(r)

        for j in range(1, len(r) + 1):
            dp[j] = F[dp[j - 1] + 1][ord(r[j - 1]) - 97]

        for i in range(1, len(l) + 1):
            dp[0] = F[dp[0] + 1][ord(l[i - 1]) - 97]

            for j in range(1, len(r) + 1):
                a = F[dp[j] + 1][ord(l[i - 1]) - 97]
                b = F[dp[j - 1] + 1][ord(r[j - 1]) - 97]
                dp[j] = min(a, b)

        return dp[-1] < n

    for i in range(len(p)):
        if interleaving(p[:i], p[i:]):
            return 'YES'
    return 'NO'


def main(n):
    # n controls both the number of test cases and string sizes
    t = max(1, n)  # number of test cases
    results = []
    for k in range(1, t + 1):
        # deterministic generation of s and p based on k and n
        len_s = max(1, n)
        len_p = max(1, n // 2 + k % (n if n > 0 else 1))

        s_chars = []
        for i in range(len_s):
            # cycle through 'a' to 'z' deterministically
            s_chars.append(chr(97 + (i + k) % 26))
        s = "".join(s_chars)

        p_chars = []
        for i in range(len_p):
            p_chars.append(chr(97 + (i * 2 + k) % 26))
        p = "".join(p_chars)

        results.append(problem(s, p))

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)