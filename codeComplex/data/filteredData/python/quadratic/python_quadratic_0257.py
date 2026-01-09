def main(n):
    # Deterministically generate a, b based on n
    if n <= 1:
        a, b = 1, 1

    else:
        # Cycle through some deterministic (a, b) pairs depending on n
        # while respecting original constraints domain (positive integers)
        pattern = [
            (1, 1),
            (1, 2),
            (2, 1),
            (1, 3),
            (3, 1),
        ]
        a, b = pattern[(n - 2) % len(pattern)]

    # Core logic from original program
    if min(a, b) > 1 or ((n, a, b) in ((2, 1, 1), (3, 1, 1))):
        # print("NO")
        pass
        return

    res = [[0] * n for _ in range(n)]
    for i in range(0, n - max(a, b)):
        res[i][i + 1] = res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in l] for l in res]

    # print("YES")
    pass
    for i in range(n):
        res[i][i] = 0
        # print(*res[i], sep='')
        pass
if __name__ == "__main__":
    main(5)