def main(n):
    # Interpret n as number of problems
    # Generate deterministic parameters
    l = n * 2
    r = n * 4
    x = max(1, n // 2)
    # Generate difficulty list c of length n
    c = [(i * 3 + 1) % (5 * n + 7) + 1 for i in range(n)]

    ans = 0
    for j in range(1 << n):
        s = 0
        num = 0
        ma = 0
        mi = 10**9
        for i in range(n):
            if j & (1 << i):
                num += 1
                s += c[i]
                if c[i] > ma:
                    ma = c[i]
                if c[i] < mi:
                    mi = c[i]
        if l <= s <= r and ma - mi >= x and num >= 2:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main(10)