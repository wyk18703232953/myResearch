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
        b = b >> 1
    return res


def inverseMod(n, m):
    return fast_mod_exp(n, m - 2, m)


def ncr(n, r, m):
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m


mod = 1000000007
f = []


def C(n):
    s = []
    mxI = 0
    for i in range(n):
        # Deterministic generation of commands:
        # First half "f", second half "s"
        if i < n // 2:
            c = "f"

        else:
            c = "s"
        s.append(c)
        if s[-1] == 'f':
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


def D(n):
    # Map n to matrix dimensions and k
    # For scalability: let rows = n, cols = n, k = n // 2
    rows = n
    cols = n
    k = n // 2

    w = [[] for _ in range(rows)]
    # Deterministic binary matrix generation using simple pattern
    # w[i][j] = '1' if (i + j) % 3 == 0 else '0'
    for i in range(rows):
        w[i] = [('1' if (i + j) % 3 == 0 else '0') for j in range(cols)]

    mn = [[0 for _ in range(k + 1)] for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(k + 1):
            c = 0
            st, en = -1, -1
            for x in range(cols):
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
            for x in range(cols - 1, -1, -1):
                if w[i - 1][x] == '1':
                    if c == j and st == -1:
                        st = x
                    if c < j:
                        c += 1
                    if c == j:
                        en = x
            if st != -1 and en != -1 >= 0:
                mn[i][j] = min(mn[i][j], st - en + 1)

    dp = [[9999999999999999 for _ in range(k + 1)] for _ in range(rows + 1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for i in range(1, rows + 1):
        for j in range(k + 1):
            for x in range(k + 1):
                if j - x >= 0:
                    val = dp[i - 1][j - x] + mn[i][x]
                    if val < dp[i][j]:
                        dp[i][j] = val

    return dp[rows][k]


def main(n):
    # For time-complexity experiments, we can run both C and D to stress algorithms.
    # Use n as the common scale; for C, command length = n; for D, matrix n x n.
    res_C = C(n)
    res_D = D(n)
    # Combine outputs deterministically to avoid unused computations
    # print(res_C, res_D)
    pass
if __name__ == "__main__":
    main(10)