def main(n):
    # Interpret n as the string length; choose k deterministically based on n
    if n <= 0:
        print(0)
        return

    # Choose k as a small fixed number or bounded by n
    k = 5 if n >= 5 else max(1, n)

    # Deterministic construction of s (length n) over alphabet {0..k-1} and -1 for '?'
    # Pattern: positions divisible by (k+1) are '?', others are (i % k)
    s = []
    for i in range(n):
        if (i % (k + 1)) == 0:
            s.append(-1)
        else:
            s.append(i % k)

    inf = 10**16
    md = 10**9 + 7  # not used but kept to preserve structure

    def ok(m):
        nxt = [[n] * (n + 1) for _ in range(k)]
        for j in range(k):
            cnt = 0
            ni = n
            nxtj = nxt[j]
            for i in range(n - 1, -1, -1):
                if s[i] == -1 or s[i] == j:
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= m:
                    ni = i
                nxtj[i] = ni
        dp = [n + 1] * (1 << k)
        dp[0] = 0
        for bit in range(1 << k):
            lpos = dp[bit]
            if lpos + m > n:
                continue
            for j in range(k):
                if (bit >> j) & 1:
                    continue
                i = nxt[j][lpos]
                if i + m <= n:
                    nbit = bit | (1 << j)
                    if dp[nbit] > i + m:
                        dp[nbit] = i + m
        return dp[-1] <= n

    l, r = 0, n // k + 1
    while l + 1 < r:
        m = (l + r) // 2
        if ok(m):
            l = m
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main(1000)