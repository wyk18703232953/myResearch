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
    # Map n to parameters for function D
    # Let size of array be n, k be max groups = max(1, n // 3)
    k = max(1, n // 3)
    # Deterministic array: a[i] = (i * 3) % 11 + i // 2
    a = [(i * 3) % 11 + (i // 2) for i in range(n)]
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
    # print(dp[n][k])
    pass


def B(n):
    # Map n to size and queries for function B
    # Use n as array length; number of queries q = max(1, n)
    size = n
    if size <= 0:
        size = 1
    q = size
    # Deterministic array a: a[i] = i % 7
    a = [i % 7 for i in range(size)]

    mat = [[0 for _ in range(size)] for _ in range(size)]
    dp_local = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                mat[i][j] = a[i]
                dp_local[i][j] = a[i]
    x = 1
    while x < size:
        j = x
        i = 0
        while j < size:
            mat[i][j] = mat[i][j - 1] ^ mat[i + 1][j]
            j += 1
            i += 1
        x += 1

    x = 1
    while x < size:
        j = x
        i = 0
        while j < size:
            dp_local[i][j] = max(mat[i][j], dp_local[i][j - 1], dp_local[i + 1][j])
            j += 1
            i += 1
        x += 1

    # Generate q deterministic queries over [1, size]
    # Query i: l = (i % size) + 1, r = size; ensure l <= r
    for i in range(q):
        l = (i % size) + 1
        r = size
        # print(dp_local[l - 1][r - 1])
        pass


def main(n):
    # Choose which core routine to exercise.
    # For this refactor, we call B with scale n.
    B(n)
    # If you want to exercise D instead for experiments, call:
    # D(n)


if __name__ == "__main__":
    # Example deterministic call for experiments
    main(10)