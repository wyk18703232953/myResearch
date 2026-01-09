def main(n):
    # n controls the number of test cases and the length of strings
    if n <= 0:
        return
    T = n
    results = []
    for case in range(T):
        # generate s and t deterministically based on case index and n
        length_s = max(1, n)
        length_t = max(1, (n // 2) + (case % max(1, n // 3 + 1)))
        s_chars = []
        t_chars = []
        for i in range(length_s):
            s_chars.append(chr(ord('a') + (i + case) % 26))
        for i in range(length_t):
            t_chars.append(chr(ord('a') + (i * 2 + case) % 26))
        s = "".join(s_chars)
        t = "".join(t_chars)

        if len(t) == 1:
            results.append("YES" if t in s else "NO")
            continue

        nxt = [[-1] * 26 for _ in range(len(s) + 1)]
        nxt[-2][ord(s[-1]) - ord('a')] = len(s) - 1
        for i in range(len(s) - 2, -1, -1):
            for c in range(26):
                nxt[i][c] = nxt[i + 1][c]
            nxt[i][ord(s[i]) - ord('a')] = i

        ans = "NO"
        for p in range(1, len(t)):
            a = t[:p]
            b = t[p:]
            dp = [[-1] * (len(b) + 1) for _ in range(len(a) + 1)]
            dp[0][0] = 0
            for la in range(len(a) + 1):
                for lb in range(len(b) + 1):
                    if dp[la][lb] != -1:
                        if la < len(a):
                            if dp[la + 1][lb] != -1:
                                if nxt[dp[la][lb]][ord(a[la]) - ord('a')] != -1:
                                    if nxt[dp[la][lb]][ord(a[la]) - ord('a')] < dp[la + 1][lb] - 1:
                                        dp[la + 1][lb] = nxt[dp[la][lb]][ord(a[la]) - ord('a')]
                                        dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])

                            else:
                                dp[la + 1][lb] = nxt[dp[la][lb]][ord(a[la]) - ord('a')]
                                dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])
                        if lb < len(b):
                            if dp[la][lb + 1] != -1:
                                if nxt[dp[la][lb]][ord(b[lb]) - ord('a')] != -1:
                                    if nxt[dp[la][lb]][ord(b[lb]) - ord('a')] < dp[la][lb + 1] - 1:
                                        dp[la][lb + 1] = nxt[dp[la][lb]][ord(b[lb]) - ord('a')]
                                        dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])

                            else:
                                dp[la][lb + 1] = nxt[dp[la][lb]][ord(b[lb]) - ord('a')]
                                dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])
                    if dp[len(a)][len(b)] != -1:
                        ans = "YES"
                        break
                if ans == "YES":
                    break
            if ans == "YES":
                break
        results.append(ans)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)