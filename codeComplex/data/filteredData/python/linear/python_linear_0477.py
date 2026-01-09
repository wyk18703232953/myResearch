def main(n):
    # Deterministically generate data based on n
    # Interpret n as the length of arrays a and c
    if n <= 0:
        # print(0)
        pass
        return

    # Generate a as a permutation with a single cycle:
    # a[i] points to (i+1) % n + 1 (1-based)
    a = [((i + 1) % n) + 1 for i in range(n)]

    # Generate c deterministically, e.g., some varying costs
    # Use a simple pattern: c[i] = (i * 7) % (n + 5) + 1 to avoid zeros
    c = [((i * 7) % (n + 5)) + 1 for i in range(n)]

    u = [0] * len(a)
    ans = 0

    for i in range(len(a)):
        if u[i] != 0:
            continue
        idx = i
        while u[idx] == 0:
            u[idx] = 1
            idx = a[idx] - 1

        if u[idx] == 2:
            idx = i
            while u[idx] == 1:
                u[idx] = 2
                idx = a[idx] - 1
            continue

        start = idx
        mn = c[idx]
        u[idx] = 2
        while a[idx] - 1 != start:
            idx = a[idx] - 1
            mn = min(mn, c[idx])
            u[idx] = 2

        idx = i
        while u[idx] == 1:
            u[idx] = 2
            idx = a[idx] - 1
        ans += mn
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)