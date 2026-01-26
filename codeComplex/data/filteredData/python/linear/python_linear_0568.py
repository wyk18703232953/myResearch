def main(n):
    if n <= 0:
        return

    # Deterministic parent array generation:
    # p[1] = 0 (unused), for i>=2, set parent as i//2 to form a fixed tree
    p = [0, 0] + [i // 2 for i in range(2, n + 1)]
    d = [0] * (n + 1)

    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]
    if n == 1:
        d[1] = 1
    d = d[1:]
    d.sort()
    # print(*d)
    pass
if __name__ == "__main__":
    main(10)