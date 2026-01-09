import math

mod = 998244353
f = []
dp = []


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
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m


def D(n):
    k = max(1, n // 5)
    a = [i % 10 for i in range(n)]
    a = sorted(a)
    cnt = [0 for _ in range(n)]
    for i in range(n):
        c = 0
        for j in range(i, n):
            if a[j] - a[i] <= 5:
                c += 1

            else:
                break
        cnt[i] = c

    global dp
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 <= k:
                dp[i + cnt[i]][j + 1] = max(dp[i + cnt[i]][j + 1], dp[i][j] + cnt[i])
    return dp[n][k]


def B(n):
    a = [i % 1000 for i in range(n)]
    q = max(1, n)

    mat = [[0 for _ in range(n)] for _ in range(n)]
    dp_local = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i][j] = a[i]
                dp_local[i][j] = a[i]
    x = 1
    while x < n:
        j = x
        i = 0
        while j < n:
            mat[i][j] = mat[i][j - 1] ^ mat[i + 1][j]
            j += 1
            i += 1
        x += 1

    x = 1
    while x < n:
        j = x
        i = 0
        while j < n:
            dp_local[i][j] = max(mat[i][j], dp_local[i][j - 1], dp_local[i + 1][j])
            j += 1
            i += 1
        x += 1

    res = []
    for i in range(q):
        l = (i % n) + 1
        r = n
        res.append(dp_local[l - 1][r - 1])
    return res


def main(n):
    if n <= 0:
        return
    _ = D(n)
    res_B = B(n)
    for v in res_B:
        # print(v)
        pass
if __name__ == "__main__":
    main(5)