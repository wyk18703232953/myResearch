import math
from functools import cmp_to_key

mod = 1000000007
f = []

def fact(n, m):
    global f
    f = [1 for _ in range(n + 1)]
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % m

def fast_mod_exp(a, b, m):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

def inverseMod(n, m):
    return fast_mod_exp(n, m - 2, m)

def ncr(n, r, m):
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m

def getCount(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count

def solve_C(s, k):
    if k == 0:
        return 1
    dp = [0 for _ in range(1010)]
    for i in range(1010):
        if i == 0 or i == 1:
            continue
        dp[i] = dp[getCount(i)] + 1
    fact(1010, mod)

    ans = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            continue
        for j in range(max(count, 1), 1010):
            if dp[j] == k - 1:
                ans = (ans + ncr(len(s) - i - 1, j - count, mod)) % mod
                if i == 0 and k == 1:
                    ans = (ans + mod - 1) % mod
        count += 1
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    if dp[count] == k - 1:
        ans = (ans + 1) % mod
    return ans

def solve_D(n, m, k, w):
    mn = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(k + 1):
            c = 0
            st, en = -1, -1
            for x in range(m):
                if w[i - 1][x] == '1':
                    if c == j and st == -1:
                        st = x
                    if c < j:
                        c += 1
                    if c == j:
                        en = x
            mn[i][j] = en - st + 1 if st != -1 and en != -1 else 0
            st, en = -1, -1
            c = 0
            for x in range(m - 1, -1, -1):
                if w[i - 1][x] == '1':
                    if c == j and st == -1:
                        st = x
                    if c < j:
                        c += 1
                    if c == j:
                        en = x
            if st != -1 and en != -1 >= 0:
                mn[i][j] = min(mn[i][j], st - en + 1)

    dp = [[9999999999999999 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(k + 1):
            for x in range(k + 1):
                if j - x >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - x] + mn[i][x])
    return dp[n][k]

def main(n):
    # Problem C input generation:
    # s: binary string of length n (alternating 1 and 0)
    # k: derived from n deterministically
    if n <= 0:
        s = "1"

    else:
        s = "".join('1' if i % 2 == 0 else '0' for i in range(n))
    k = max(1, (n % 10) + 1)

    ans_C = solve_C(s, k)

    # Problem D input generation:
    # n_rows, m_cols, k_ones based on n
    n_rows = max(1, n // 3)
    m_cols = max(1, (n // 2) or 1)
    k_ones = min(m_cols, max(0, n_rows // 2))

    w = []
    for i in range(n_rows):
        row = []
        for j in range(m_cols):
            # deterministic pattern: '1' if (i+j) divides (n_rows + m_cols) else '0'
            if (i + j + 1) % ((n_rows + m_cols) or 1) == 0:
                row.append('1')

            else:
                row.append('0')
        w.append(row)

    ans_D = solve_D(n_rows, m_cols, k_ones, w)

    # print(ans_C)
    pass
    # print(ans_D)
    pass
if __name__ == "__main__":
    main(1000)