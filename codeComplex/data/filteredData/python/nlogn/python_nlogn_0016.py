def main(n):
    # Interpret n as number of points
    # Deterministically generate a list of (x, r) pairs
    # Example pattern: x increases by 2, r is cyclic in [1..5]
    a = [[2 * i, (i % 5) + 1] for i in range(n)]
    a.sort()
    t = n  # scale t with n in a deterministic way

    v = 2
    for i in range(n - 1):
        d = 2 * a[i + 1][0] - a[i + 1][1] - 2 * a[i][0] - a[i][1]
        if d > 2 * t:
            v += 2
        elif d == 2 * t:
            v += 1
    print(v)


if __name__ == "__main__":
    main(10)