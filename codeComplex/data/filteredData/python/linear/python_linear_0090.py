def main(n):
    a = [0] * n
    dp = [0] * n
    for i in range(n):
        x = i
        p = (i * 2) % (n + 1 if n > 0 else 1)
        a[i] = (x, p)
    a.sort()
    for i in range(n):
        x, p = a[i]
        l = -1
        r = n
        v = x - p
        while r - l > 1:
            c = (l + r) // 2
            if a[c][0] >= v:
                r = c

            else:
                l = c
            if l == -1:
                dp[i] = i - l - 1

            else:
                dp[i] = i - l - 1 + dp[l]
    z = 10**9
    for i in range(n):
        z = min(z, dp[i] + n - i - 1)
    # print(z)
    pass
if __name__ == "__main__":
    main(10)