def main(n):
    # Deterministically generate parent array p[2..n]
    # p[i] is in [1, i-1], forming a rooted tree with root 1
    if n <= 0:
        return
    p = [0, 0]
    for i in range(2, n + 1):
        # simple deterministic parent generation
        p.append((i // 2) if (i // 2) >= 1 else 1)

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