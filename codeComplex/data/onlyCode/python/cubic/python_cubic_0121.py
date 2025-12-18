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


for _ in range(int(input())):
    print(problem(input(), input()))
