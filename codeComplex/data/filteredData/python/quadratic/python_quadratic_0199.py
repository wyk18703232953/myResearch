#!/usr/bin/env python3

def main(n):
    # n: length of array a and also number of queries q (for scaling)
    if n <= 0:
        return

    # Deterministic construction of a
    # Example pattern: a[i] = (i * 17 + 23) ^ (i // 2)
    a = [((i * 17 + 23) ^ (i // 2)) for i in range(n)]

    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        f[i][i] = dp[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # Deterministic construction of q queries
    # q = n, queries cover various ranges in [1, n]
    q = n
    for k in range(q):
        # l and r in 1-based indexing, ensure l <= r
        l = (k % n) + 1
        r = ((k * 7) % n) + 1
        if l > r:
            l, r = r, l
        # print(dp[l - 1][r - 1])
        pass
if __name__ == "__main__":
    main(5)