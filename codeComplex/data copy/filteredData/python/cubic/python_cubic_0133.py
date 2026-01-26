import sys


def solve_case(s, t):
    s = [ord(x) - 97 for x in s]
    t = [ord(x) - 97 for x in t]
    n, m = len(s), len(t)
    nxt = [[n + 1] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1][:]
        nxt[i][s[i]] = i
    for b in range(m):
        t1 = t[:b]
        t2 = t[b:]
        dp = [[n + 1] * (m - b + 1) for _ in range(b + 1)]
        dp[0][0] = 0
        for j in range(b + 1):
            for k in range(m - b + 1):
                if j:
                    dp[j][k] = min(dp[j][k], nxt[dp[j - 1][k]][t1[j - 1]] + 1)
                if k:
                    dp[j][k] = min(dp[j][k], nxt[dp[j][k - 1]][t2[k - 1]] + 1)
        if dp[b][m - b] <= n:
            return "YES"
    return "NO"


def deterministic_string(length, shift):
    # cycle through 'a'..'z' deterministically with a phase shift
    return "".join(chr(97 + ((i + shift) % 26)) for i in range(length))


def main(n):
    # interpret n as both:
    # - the number of test cases T
    # - and the base length for strings, scaled slightly per test
    if n <= 0:
        return
    T = n
    results = []
    for i in range(1, T + 1):
        # lengths grow linearly with i to vary input size inside the same n
        len_s = max(1, n + i // 2)
        len_t = max(1, n // 2 + i // 3)
        s = deterministic_string(len_s, i)
        t = deterministic_string(len_t, i * 7)
        res = solve_case(s, t)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # example deterministic run
    main(5)