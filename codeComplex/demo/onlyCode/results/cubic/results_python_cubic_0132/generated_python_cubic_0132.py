def main(n):
    import random
    import string
    random.seed(0)
    test = n
    results = []
    for _ in range(test):
        s_len = max(1, n // 2)
        t_len = max(1, n // 3)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(s_len))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(t_len))
        n_s = len(s)
        m_t = len(t)
        pos = [[1000 for _ in range(26)] for _ in range(n_s + 2)]
        for i in range(n_s, -1, -1):
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
            results.append("YES")
        else:
            results.append("NO")
    for r in results:
        print(r)
    return results

if __name__ == "__main__":
    main(10)