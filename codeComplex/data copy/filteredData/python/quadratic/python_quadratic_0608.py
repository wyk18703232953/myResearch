base = 1000000007

def main(n):
    # n controls the length of array a
    if n <= 0:
        # print(0)
        pass
        return
    m = max(1, n // 3)  # make m grow with n but m <= n
    k = 5               # fixed deterministic constant

    a = [(i * 7 + 3) % 100 for i in range(n)]

    mx = 0
    dp = []
    dd = []
    for j in range(m):
        for i in range(n + 1):
            dp.append(base)
            dd.append(0)
        for i in range(n):
            dd[i + 1] = dd[i] + a[i] - k * (i % m == j)
            if i == 0:
                dp[i + 1] = min(0, dp[i])

            else:
                dp[i + 1] = min(dd[i], dp[i])
            if i % m == j:
                mx = max(mx, dd[i + 1] - dp[i + 1])
    # print(mx)
    pass
if __name__ == "__main__":
    main(10)