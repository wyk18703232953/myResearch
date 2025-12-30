import math
import random

def calc(st, j):
    ans = 10**30
    if j >= len(st):
        return 0
    j = len(st) - j
    for i in range(j - 1, len(st)):
        ans = min(ans, st[i] - st[i - j + 1] + 1)
    return ans

def solve(n, m, k, s):
    inf = 10**30
    dp = [[inf for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        st = []
        for ik in range(len(s[i - 1])):
            if s[i - 1][ik] == '1':
                st.append(ik)
        for j in range(k + 1):
            no = calc(st, j)
            for t in range(k + 1 - j):
                dp[i][t + j] = min(dp[i][t + j], no + dp[i - 1][t])
    return dp[n][k]

def generate_test_data(n):
    # Scale other parameters based on n
    m = max(1, n)          # length of each string
    k = min(n, m)          # number of deletions allowed

    s = []
    for _ in range(n):
        # generate a random binary string of length m
        row = ''.join(random.choice('01') for _ in range(m))
        s.append(row)
    return n, m, k, s

def main(n):
    n, m, k, s = generate_test_data(n)
    ans = solve(n, m, k, s)
    print(ans)

if __name__ == "__main__":
    # example: run with n = 5
    main(5)