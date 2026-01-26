#!/usr/bin/env python3

def main(n):
    if n <= 0:
        return
    # 构造数组长度 n
    a = [(i * 17 + 3) ^ (i // 2) for i in range(n)]

    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        f[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]
    for i in range(n - 1, -1, -1):
        dp[i][i] = f[i][i]
        for j in range(i + 1, n):
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # 构造 q 组询问，q 与 n 成比例
    q = max(1, n)
    for k in range(q):
        # l, r 在 1..n 范围内，且 l <= r
        l = (k % n) + 1
        r = n - (k % n)
        if l > r:
            l, r = r, l
        # print(dp[l - 1][r - 1])
        pass
if __name__ == "__main__":
    main(5)