def check(s, t1, t2):
    s1 = len(t1)
    s2 = len(t2)
    n = len(s)
    dp = [[-1] * (s1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(s1 + 1):
            if dp[i][j] >= 0:
                if j < s1 and t1[j] == s[i]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                if dp[i][j] < s2 and t2[dp[i][j]] == s[i]:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    if dp[n][s1] == s2:
        return True
    else:
        return False


def solve(s, t):
    le = len(t)
    for i in range(le):
        t1 = t[:i]
        t2 = t[i:]
        if check(s, t1, t2) == True:
            return "YES"
    return "NO"


def main(n):
    results = []
    for _ in range(n):
        s = "abacaba" * ((n % 5) + 1)
        t = "aba" * ((n % 3) + 1)
        res = solve(s, t)
        results.append(res)
    return results


if __name__ == "__main__":
    print(main(3))