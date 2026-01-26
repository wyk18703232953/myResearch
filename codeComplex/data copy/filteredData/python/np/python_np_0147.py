def main(n):
    # Generate deterministic intervals d based on n
    # Each pair (l, r) satisfies 0 <= l < r
    d = []
    for i in range(n):
        l = i % 50
        r = l + 1 + (i // 50) % 50
        d.append([l, r])

    s = 0.0

    for k in range(1, 10001):
        p = [min(max((k - l) / (r - l + 1), 1e-20), 1) for l, r in d]

        u = 1.0
        v = 1.0

        for r in p:
            u *= r

        for r in p:
            v *= r
            s += (u - v) * (r - 1) / r

    print(s)


if __name__ == "__main__":
    main(1000)