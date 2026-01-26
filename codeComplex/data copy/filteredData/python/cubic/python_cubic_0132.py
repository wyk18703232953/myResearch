def main(n):
    # Generate deterministic test cases based on n
    # For experiment purposes, we create n test cases
    # Each test case has strings s and t whose lengths depend on the test index
    test = n

    for idx in range(test):
        # Deterministic lengths for s and t
        len_s = max(1, (idx % 10) + 5)       # between 5 and 14
        len_t = max(1, (idx % 7) + 3)        # between 3 and 9

        # Generate s and t deterministically using simple arithmetic on index
        s = ''.join(chr(ord('a') + ((idx * 7 + i * 3) % 26)) for i in range(len_s))
        t = ''.join(chr(ord('a') + ((idx * 11 + i * 5) % 26)) for i in range(len_t))

        # Core algorithm logic from original program
        n_s = len(s)
        m_t = len(t)
        pos = [[1000 for _ in range(26)] for _ in range(n_s + 2)]
        for i in range(n_s + 1)[::-1]:
            if i < n_s:
                for j in range(26):
                    pos[i][j] = pos[i + 1][j]
            if i > 0:
                x = ord(s[i - 1]) - 97
                pos[i][x] = i
        flg = 0
        for i in range(m_t):
            t1 = t[:i]
            t2 = t[i:]
            m1 = len(t1)
            m2 = len(t2)
            dp = [[1000 for _ in range(m2 + 1)] for _ in range(m1 + 1)]
            dp[0][0] = 0
            for j in range(m1 + 1):
                for k in range(m2 + 1):
                    if j > 0 and dp[j - 1][k] < 1000:
                        t1x = ord(t1[j - 1]) - 97
                        dp[j][k] = min(dp[j][k], pos[dp[j - 1][k] + 1][t1x])
                    if k > 0 and dp[j][k - 1] < 1000:
                        t2x = ord(t2[k - 1]) - 97
                        dp[j][k] = min(dp[j][k], pos[dp[j][k - 1] + 1][t2x])
            if dp[-1][-1] < 1000:
                flg = 1
                break
        if flg:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # Example deterministic run with input scale n = 5
    main(5)