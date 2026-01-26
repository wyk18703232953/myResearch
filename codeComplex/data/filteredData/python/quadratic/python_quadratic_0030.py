import math

mod = 1000000007
f = []

def fact(n, m):
    global f
    f = [1 for _ in range(n + 1)]
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

def D(n, m, k, w):
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

def C(n, s):
    mxI = 0
    for i in range(n):
        if s[i] == 'f':
            mxI += 1
    dp = [[0 for _ in range(mxI + 1)] for _ in range(n)]
    dp[0][0] = 1
    preSum = [1 for _ in range(mxI + 1)]
    pre = 1
    for i in range(1, n):
        pre = 0
        for j in range(mxI + 1):
            if s[i - 1] == 'f':
                if j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] % mod

                else:
                    dp[i][j] = 0

            else:
                dp[i][j] = (preSum[mxI] % mod - (pre if j != 0 else 0) % mod) % mod
            pre = preSum[j]
            preSum[j] = (((preSum[j - 1] if j != 0 else 0) % mod) + dp[i][j] % mod) % mod
    return preSum[mxI] % mod

def generate_C_input(n):
    # Deterministic pattern: half 'f', half 's' (or nearby)
    s = []
    for i in range(n):
        if i % 2 == 0:
            s.append('f')

        else:
            s.append('s')
    return s

def generate_D_input(n):
    # Map n to (rows, cols, k) and construct a deterministic binary matrix
    # Let rows = n, cols = max(1, n // 2), k = min(rows, cols, max(1, n // 3))
    rows = max(1, n)
    cols = max(1, n // 2)
    k = max(1, min(rows, cols, max(1, n // 3)))
    w = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Deterministic pattern: '1' if (i + j) is even, else '0'
            row.append('1' if (i + j) % 2 == 0 else '0')
        w.append(row)
    return rows, cols, k, w

def main(n):
    # Use both parts to make the workload scale with n
    s = generate_C_input(max(1, n))
    res_C = C(len(s), s)
    rows, cols, k, w = generate_D_input(max(1, n // 2))
    res_D = D(rows, cols, min(k, cols), w)
    # print(res_C, res_D)
    pass
if __name__ == "__main__":
    main(10)