def main(n):
    if n <= 0:
        print(0)
        return

    # Deterministic generation of input data of size n
    # a[i] = (x_i, p_i), x strictly increasing so that sort() keeps order
    a = []
    for i in range(n):
        x = 2 * i + 1
        p = (i * i + 3 * i + 7) % (n + 5)
        a.append((x, p))

    a.sort()
    dp = [0] * n

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

    z = 1e9
    for i in range(n):
        z = min(z, dp[i] + n - i - 1)
    print(z)


if __name__ == "__main__":
    main(10)